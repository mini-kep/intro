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

Jane is well-versed in using FRED or quandl, and for Russian or custom statistics she wants:

- a clean dataset with latest data from different sources that she can access at one place 
- browse what data is available
- read this data on a local machine:
   - as pd.DataFrame 
   - as R dataframe  

Jane also finds it useful to:
- see what other people code with this data
- make a dashboard for macroeconomic indicators that interest her (boss)
- view a dashboard on a smartphone / get notifications 
- something else?


Dataflow
========

The project pipeline is as follows:

```

data sources -> parsers -> scheduler -> | -> database -> | -> custom API -> pandas dataframe
                                        |                |
                          (Optional:  REST API        REST API)

``` 


The latest about pipeline is [here](https://github.com/mini-kep/intro/blob/master/pipeline/pipeline.py)

Earlier comments: 

0. Common namespace
   - convention on how to name variables 
   - convention on how to refer to original data sources

1. parsers on static files or other APIs
   - download data
   - assign variable names from common namespace 
   - provide output in json on call ("fetch all", "fetch after <date>")   

2. parser scheduler / database import broker
   - establish expected database content based on current date 
   - query parsers to get expected data 
   - resolve import conflicts (overwriting data on revision or same data from different sources)
   - upload to database

3. database 
   - flask app on top of SQLAlchemy with Postgres backend 
   - very generic component with little custom functionality

4. front end app (flask)
   - html content for viewing
   - end-user API(s)

5. end-user examples/solutions
   - data access examples for end-user API
   - [charting macroeconimic data](https://github.com/mini-kep/user-charts)
   - models in jupiter notebooks

# Project repos

| Repo | Tests | Coverage |
| ---- | ----- | -------- |
| [parser-rosstat-kep](https://github.com/mini-kep/parser-rosstat-kep) | [![](https://travis-ci.org/mini-kep/parser-rosstat-kep.svg?branch=master)](https://travis-ci.org/mini-kep/parser-rosstat-kep) | [![](https://codecov.io/gh/mini-kep/parser-rosstat-kep/branch/master/graphs/badge.svg)](https://codecov.io/gh/mini-kep/parser-rosstat-kep) |
| [parsers](https://github.com/mini-kep/parsers) | [![](https://travis-ci.org/mini-kep/parsers.svg?branch=master)](https://travis-ci.org/mini-kep/parsers) | [![](https://codecov.io/gh/mini-kep/parsers/branch/master/graphs/badge.svg)](https://codecov.io/gh/mini-kep/parsers) |
| [db](https://github.com/mini-kep/db) |  |  |
| [frontend-app](https://github.com/mini-kep/frontend-app) | [![](https://travis-ci.org/mini-kep/frontend-app.svg?branch=master)](https://travis-ci.org/mini-kep/frontend-app) | [![](https://codecov.io/gh/mini-kep/frontend-app/branch/master/graphs/badge.svg)](https://codecov.io/gh/mini-kep/frontend-app) |
| [full-app](https://github.com/mini-kep/full-app) | [![](https://travis-ci.org/mini-kep/full-app.svg?branch=master)](https://travis-ci.org/mini-kep/full-app) | [![](https://codecov.io/gh/mini-kep/full-app/branch/master/graphs/badge.svg)](https://codecov.io/gh/mini-kep/full-app) |


# New to project?

Try [new user checklist](https://github.com/mini-kep/intro/wiki/New-user-checklist).


# Changelog
- **2017-09-28** new data pipeline description [open for comments](https://github.com/mini-kep/intro/issues/14) 
- **2017-09-28** <https://github.com/mini-kep/parsers> provide data from three parsers (macro, oil, fx)
- **2017-09-07** flask app <http://mini-kep.herokuapp.com/> relays parsing results from 
                 <https://github.com/mini-kep/parser-rosstat-kep>  


