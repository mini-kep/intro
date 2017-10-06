Dataflow
========

The project data pipeline is the following:

 1. data sources and parsers 
 2. scheduler
 3. database 
 4. custom API
 5. use cases 


(1) Data sources and parsers
----------------------------


Data sources are static files (Word, PDF, html) and some open APIs. Parser is python code performing requests and emitting datapoints. 

[parser-rosstat-kep](https://github.com/mini-kep/parser-rosstat-kep) parser supplies most time series. 
It is supplemented by daily ruble exchange rate from Bank of Russia and oil prices from EIA and some others.

Aggratation of parser data is made at [parsers/runner.py](https://github.com/mini-kep/parsers/blob/master/parsers/runner.py)

[parser-rosstat-kep](https://github.com/mini-kep/parser-rosstat-kep):
[![](https://travis-ci.org/mini-kep/parser-rosstat-kep.svg?branch=master)](https://travis-ci.org/mini-kep/parser-rosstat-kep) 
[![](https://codecov.io/gh/mini-kep/parser-rosstat-kep/branch/master/graphs/badge.svg)](https://codecov.io/gh/mini-kep/parser-rosstat-kep)

[parsers](https://github.com/mini-kep/parsers):
[![](https://travis-ci.org/mini-kep/parsers.svg?branch=master)](https://travis-ci.org/mini-kep/parsers)
[![](https://codecov.io/gh/mini-kep/parsers/branch/master/graphs/badge.svg)](https://codecov.io/gh/mini-kep/parsers) 


(2) Scheduler
---------------

Scheduler is not implemented yet, but it is a cron-like task list to invoke parsers and upload data to database. 


(3) Database
------------

Database is a flask/django app that allow POST data in database and quiry it with GET method. 

Example:

- <https://minikep-db.herokuapp.com/api/datapoints?name=BRENT&freq=d&start_date=2017-01-01>


There is a specification for database layer and two implementations: in flask and in django, done at slightly different time by different people. Ideally, they should both comply to specification and simplified http POST/GET tests.

- db layer spec: <https://github.com/mini-kep/db/blob/master/SPEC.md>
- http tests: <https://github.com/mini-kep/db/blob/master/requests_tests.py>

**Flask** implementation is in active development: 

- flask database: <https://github.com/mini-kep/db/tree/flask_sqlalchemy> (active)

flask [db](https://github.com/mini-kep/full-app): 
[![Build Status](https://travis-ci.org/mini-kep/db.svg?branch=flask_sqlalchemy)](https://travis-ci.org/mini-kep/db)

**Django** implementation is now dormant.

The reason to have two apps is to try both flask and django. With django the idea was that all components could go into one project, but django app seems slightly harder to maintain.

django [full-app](https://github.com/mini-kep/full-app): 
[![](https://travis-ci.org/mini-kep/full-app.svg?branch=master)](https://travis-ci.org/mini-kep/full-app) 
[![](https://codecov.io/gh/mini-kep/full-app/branch/master/graphs/badge.svg)](https://codecov.io/gh/mini-kep/full-app) 


(4) Custom API 
--------------
Custom API simplified interface for end-user queries. 

Custom API endpoint is a long URL at a frontend flask app that translates this URL to a database query and supplies data as json readable by ```pd.read_json()```

Example (returns its parameters, not implemented):
- <http://mini-kep.herokuapp.com/ru/series/BRENT/m/eop/2017>

Frontend flask app also provides a showcase for the variables - the variable list and homepages for the individual indicators. 
This functionality is not implemented yet.

[frontend-app](https://github.com/mini-kep/frontend-app):
[![](https://travis-ci.org/mini-kep/frontend-app.svg?branch=master)](https://travis-ci.org/mini-kep/frontend-app)  [![](https://codecov.io/gh/mini-kep/frontend-app/branch/master/graphs/badge.svg)](https://codecov.io/gh/mini-kep/frontend-app)

(5) Use cases
-------------

Use cases  are sample visualisations and models relying on data from custom API.

There is a [repo for use cases](https://github.com/mini-kep/user-charts), but it is practically empty, as I'm busy constructing the data pipeline.

The use cases may resemble [datachart.cc](http://datachart.cc/)  or [datalab](https://github.com/epogrebnyak/data-lab).


Changelog
=========

- **2017-10-06** db POST/GET implemented <https://minikep-db.herokuapp.com/api/datapoints?name=BRENT&freq=d>
- **2017-09-28** new data pipeline description [open for comments](https://github.com/mini-kep/intro/issues/14) 
- **2017-09-28** <https://github.com/mini-kep/parsers> provide data from three parsers (macro, oil, fx)
- **2017-09-07** flask app <http://mini-kep.herokuapp.com/> relays parsing results from 
                 <https://github.com/mini-kep/parser-rosstat-kep>                  
