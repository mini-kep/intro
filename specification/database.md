Overview
========

This document describes database layer in between parsers and end-user API:

Expected fucntionality:
- parser delivers a list of dicts, each dict is a datapoint
- database should have a POST method at ```api\incoming``` and write incoming json to db
- POST operation must have some authentication
- for simplicity all data is upserted - newer data always overwrites older data
- database has GET method has datapoint keys and parameters (variable name, frequency), 
- GET retruns same format of output as incoming, output ordered by date,  optionally    
  filtered by start date and end date 

Database schema
===============

Table **Datpoint**
```
Id – UID, autoincrement  
Name – type String \*  eg GDP
Freq – type String \*  
Date – type DateTime \*  2016-12-31
Value – Float  

\* - composite key
```

See example at <https://github.com/mini-kep/db/blob/master/demo/sqlalchemy/datapoint.py>

Data structures
===============

#### Data structure - incoming json

Incoming json should have a structure like
    [{
        "date": "1999-03-31",
        "freq": "q",
        "name": "INVESTMENT_bln_rub",
        "value": 12345.6
    },
    {...} 
    ]



Database methods
================

POST
----

```POST api/incoming``` 

Validates incoming json and upsert values to database. All fields should be filled.

For insert_many() operation see *sheep/flock* example at <https://stackoverflow.com/a/33768160/1758363>

Returns:
- empty JSON on success
- error 400 if there’s an error in incoming json (eg invalid date string or empty parameter or missing field)

Parser result is obtained by  ```Dataset.yield_dicts(start='2017-01-01')``` in <https://github.com/mini-kep/parsers/blob/master/parsers/runner.py>, see ```Dataset.serialise()``` for json creation.

Other examples of incoming json:
- a large (1.8M) json is [located here](https://github.com/mini-kep/intro/blob/master/pipeline/dataset.json)
- sample data is presented [here](https://github.com/mini-kep/full-app/issues/9#issuecomment-331814995)

GET (REST)
----------

```
GET api/datapoints?name=<name>&freq=<freq>
GET api/datapoints?name=<name>&freq=<freq>&start_date=<start_date>&end_date=<end_date>
```

Parameters:
name – name value to search like name=BRENT
freq – freq value to search like freq=m
start_date(optional) –  return results with date greater than this parameter
end_date(optional) – return results with date less than this parameter

Returns:
- JSON in format similar to incoming json with data sorted by date
- empty JSON if there’s no data with such query.

Method validates parameters and returns error 400 if there’s an error in parameters (like string in data parameter or empty parameter) 

Security
========

POST methods should require API_TOKEN as URL parameter or header, validate it with environment variable (possibly Heroku config vars)

Tests
=====

Upload data from JSON to DB, run python unit tests with requests to different methods, validate them with uploaded data.
Use combinations GET – POST – GET to validate data inserts and updates.
[Example1](https://github.com/mini-kep/db/blob/master/demo/sqlalchemy/tests/test_clientdb_demo.py)
[Example2](https://github.com/mini-kep/full-app/blob/master/datapoint/tests.py)

Should we write some tests in curl/httpie? http tests: <https://github.com/mini-kep/db/blob/master/requests_tests.py>

Tech stack
==========

Web-frameworks: Flask + SQLAlchemy or Django, may consider Falcon

Container: prototype deployed to Heroku, may also use AWS

Database: Postgres (default on Heroku) or RDS on AWS

Repositories
============

The database layer is to be developed here, at ```db``` repo: <https://github.com/mini-kep/db>


flask [db](https://github.com/mini-kep/db): 
[![Build Status](https://travis-ci.org/mini-kep/db.svg?branch=master)](https://travis-ci.org/mini-kep/db)

There is also [django project for database](django_app.md),  but it is on hold now.

Discussion
==========

<https://github.com/mini-kep/db/issues/5>
