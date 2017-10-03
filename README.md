| Repo | Tests | Coverage |
| ---- | ----- | -------- |
| [parser-rosstat-kep](https://github.com/mini-kep/parser-rosstat-kep) | [![](https://travis-ci.org/mini-kep/parser-rosstat-kep.svg?branch=master)](https://travis-ci.org/mini-kep/parser-rosstat-kep) | [![](https://codecov.io/gh/mini-kep/parser-rosstat-kep/branch/master/graphs/badge.svg)](https://codecov.io/gh/mini-kep/parser-rosstat-kep) |
| [parsers](https://github.com/mini-kep/parsers) | [![](https://travis-ci.org/mini-kep/parsers.svg?branch=master)](https://travis-ci.org/mini-kep/parsers) | [![](https://codecov.io/gh/mini-kep/parsers/branch/master/graphs/badge.svg)](https://codecov.io/gh/mini-kep/parsers) |
| [db](https://github.com/mini-kep/db) |  |  |
| [frontend-app](https://github.com/mini-kep/frontend-app) | [![](https://travis-ci.org/mini-kep/frontend-app.svg?branch=master)](https://travis-ci.org/mini-kep/frontend-app) | [![](https://codecov.io/gh/mini-kep/frontend-app/branch/master/graphs/badge.svg)](https://codecov.io/gh/mini-kep/frontend-app) |
| [full-app](https://github.com/mini-kep/full-app) | [![](https://travis-ci.org/mini-kep/full-app.svg?branch=master)](https://travis-ci.org/mini-kep/full-app) | [![](https://codecov.io/gh/mini-kep/full-app/branch/master/graphs/badge.svg)](https://codecov.io/gh/mini-kep/full-app) |


Why another database for macroeconomic data?
============================================

- Machine-readable datafeeds for economic data are growing ([FRED](https://research.stlouisfed.org/docs/api/fred/), 
  [quandl](https://blog.quandl.com/api-for-economic-data), 
  [OECD](https://data.oecd.org/api), 
  [World Bank](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589), 
  [EIA](https://www.eia.gov/opendata/)). Please take a minute to fill [our poll about economics datasources](https://goo.gl/2wY43R) and see the results.  

- However, some data is still left in the dark. Russian macroeconomic statistics seems very fragmented (HTML, Word, Excel are common dessimination formats). This is a roadblock to reproducible analysis as dirty data escalates costs of model maintenance.      

- ```mini-kep``` aims to remove this roadblock by providing 
  [public API for Russian macroeconomic data](http://mini-kep.herokuapp.com/) 
  and examples of economic research/business planning/marketing  problems solved in python pandas or R.
  
 
User case
=========

Anna is well-versed in using FRED or quandl, and for Russian or custom statistics she wants:

- a clean dataset with latest data from different sources
- browse what data is available
- read this data on a local machine:
   - as pd.DataFrame 
   - as R dataframe  

New to project?
===============

Try [new user checklist](https://github.com/mini-kep/intro/wiki/New-user-checklist).

Dataflow
========

The project data pipeline is the following:
- data sources (static files and open APIs)
- parsers (python code performing requests and emitting datapoints) 
- scheduler (not implemented yet: periodically run parsers and upload to database)
- database (flask/django apps that allow POST data in database and quiry it with GET method)
- custom API (simplified interface for end-user queries)
- use cases (sample visualisations / models using the data from custom API)

#### Data sources and parsers

The main datasource is a parser for Rosstat KEP publication, supplemented by daily ruble exchange rate and oil prices from EIA. Responsiblility for parser data aggratation is at [parsers/runner.py]()

#### Scheduler

Scheduler is not implemented yet, but it is a cron-like task list to invoke parsers and upload data to database. 

#### Database

There is a specification for database layer and two implementations: in flask and in django, done at slightly different time by different people. Ideally, they should both comply to specification and simplified http POST/GET tests.

The reason to have two apps is to try both flask and django, only one is likely to be a production database. 

#### Custom API 

Custom API is a long URL at a frontend flask app that translates this URL to a database query and supplies data as json readable
by ```pd.read_json()```

Frontend flask app also provides a showcase for the variables - the variable list and homepages for the individual indicators. This functionality is not implemented yet.

#### Use cases

There is a repo for use cases, but it is currently practically empty, as I'm busy constructing the data pipeline.
The use cases can resemble datachart.cc  or datalab, add links.


# Changelog
- **2017-09-28** new data pipeline description [open for comments](https://github.com/mini-kep/intro/issues/14) 
- **2017-09-28** <https://github.com/mini-kep/parsers> provide data from three parsers (macro, oil, fx)
- **2017-09-07** flask app <http://mini-kep.herokuapp.com/> relays parsing results from 
                 <https://github.com/mini-kep/parser-rosstat-kep>  
                 
