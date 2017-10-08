What happens next
=================

Critical path
-------------

1. custom api -> use cases

2. scheduler -> db updates

3. ```eop``` / ```avg``` aggregation for price data


All tasks
---------

- [ ] custom API migrates to db layer, frontend-app does two things: relaying data + doing html views, flask db does no html views, but provides API endpoint 
- [ ] db flask tests extended
- [ ] consistency checks as in kep parser
- [ ] new version of db spec reflects reuired changes, db API spec can be writetn in swagger/apiary
- [ ] all specs found a new home somewhere - eg. intro/specification
- [ ] need a simple scheduler to update info: the task to run + cron-like invoker
- [ ] fronend should have indicator homepages
- [ ] fronend should have indicator listing
- [ ] django app frozen / renamed 
- [ ] finished testing existing parsers
- [ ] started parser-rosstat-isep
- [ ] maintainer found for 806 parser
- [ ] infra: herokus transferred, some paid



Dataflow
========

The project data pipeline is the following:

 1. data sources and parsers 
 2. scheduler
 3. database 
 4. custom API
 5. frontend
 6. use cases 


(1) Data sources and parsers
----------------------------

Data sources are static files (Word, PDF, html) and some open APIs. Parser is the python code performing requests and emitting datapoints. 

[parser-rosstat-kep](https://github.com/mini-kep/parser-rosstat-kep) supplies most time series. It is supplemented by daily ruble exchange rate from Bank of Russia and oil prices from EIA and some others.

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

GET example:

- <https://minikep-db.herokuapp.com/api/datapoints?name=BRENT&freq=d&start_date=2017-01-01>

Specification:
- db layer spec: <https://github.com/mini-kep/db/blob/master/SPEC.md>
- http tests: <https://github.com/mini-kep/db/blob/master/requests_tests.py>

Flask implementation: 

- flask database: <https://github.com/mini-kep/db/tree/flask_sqlalchemy> (active)

flask [db](https://github.com/mini-kep/full-app): 
[![Build Status](https://travis-ci.org/mini-kep/db.svg?branch=flask_sqlalchemy)](https://travis-ci.org/mini-kep/db)


(4) Custom API 
--------------
Custom API simplified interface for end-user queries. 

Custom API endpoint is a long URL at a frontend flask app that translates this URL to a database query and supplies data as json readable by ```pd.read_json()```

Example (returns its parameters, not implemented):
- <http://mini-kep.herokuapp.com/ru/series/BRENT/m/eop/2017>

[frontend-app](https://github.com/mini-kep/frontend-app):
[![](https://travis-ci.org/mini-kep/frontend-app.svg?branch=master)](https://travis-ci.org/mini-kep/frontend-app)  [![](https://codecov.io/gh/mini-kep/frontend-app/branch/master/graphs/badge.svg)](https://codecov.io/gh/mini-kep/frontend-app)


(5) Frontend
------------

Frontend flask app also provides a showcase for the variables - the variable list and homepages for the individual indicators. 

This functionality is not implemented yet.

Stub for indicator homepage: <http://mini-kep.herokuapp.com/ru/series/BRENT>


(6) Use cases
-------------

Use cases  are sample visualisations and models relying on data from custom API.

There is a [repo for use cases](https://github.com/mini-kep/user-charts), but it is practically empty, as I'm busy constructing the data pipeline.

The use cases may resemble [datachart.cc](http://datachart.cc/)  or [datalab](https://github.com/epogrebnyak/data-lab).


Comments
--------

#### Django db app 

There is a supplementary dfango app for the db layer. We wanted to try both flask and django. With django the idea was that all components could go into one project, but django app seems slightly harder to maintain.

django [full-app](https://github.com/mini-kep/full-app): 
[![](https://travis-ci.org/mini-kep/full-app.svg?branch=master)](https://travis-ci.org/mini-kep/full-app) 
[![](https://codecov.io/gh/mini-kep/full-app/branch/master/graphs/badge.svg)](https://codecov.io/gh/mini-kep/full-app) 


Changelog
=========

- **2017-10-06** db POST/GET implemented <https://minikep-db.herokuapp.com/api/datapoints?name=BRENT&freq=d>
- **2017-09-28** new data pipeline description [open for comments](https://github.com/mini-kep/intro/issues/14) 
- **2017-09-28** <https://github.com/mini-kep/parsers> provide data from three parsers (macro, oil, fx)
- **2017-09-07** flask app <http://mini-kep.herokuapp.com/> relays parsing results from 
                 <https://github.com/mini-kep/parser-rosstat-kep>                  
