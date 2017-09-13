Why another database for macroeconomic data?
============================================

- Machine-readable datafeeds for economic data are growing ([FRED](https://research.stlouisfed.org/docs/api/fred/), 
  [quandl](https://blog.quandl.com/api-for-economic-data), 
  [OECD](https://data.oecd.org/api), 
  [World Bank](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589), 
  [EIA](https://www.eia.gov/opendata/)), but some data is left in the dark.

- Russian macroeconomic statistics seems very fragmented (HTML, Word, Excel are common dessimination formats). 
  This is a roadblock to reproducible analysis as dirty data escalates costs of modelling/forecasting.      

- ```mini-kep``` aims to remove this roadblock by providing 
  [public API for Russian macroeconomic data](http://mini-kep.herokuapp.com/) 
  and examples of problems solved in economic research/business planning/marketing 
  (using python pandas or R).

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


Data pipeline / workflow 
========================

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
   - flask app with RESTful API on top of SQLAlchemy with Postgres backend 
   - very generic component with little custom functionality

4. front end app (flask)
   - html content for viewing
   - end-user API(s)

5. end-user examples/solutions
   - data access examples for end-user API
   - [charting macroeconimic data](https://github.com/mini-kep/user-charts)
   - models in jupiter notebooks

#### Component status

| Component         | What is happening              | 
| ----------------- | -------------------------------| 
| Naming convention |                                |
| Parsers           |  making parser template        |
| - kep             |  [working][kep]                |
| Scheduler         |                                |
| Database          |  CRUD tests for SQL Alchemy    |
| Front end app     |  [working][frontend]           |
| User cases        |                                |

[kep]: https://github.com/mini-kep/parser-rosstat-kep
[frontend]: https://github.com/mini-kep/frontend-app

# Repo list

- Intro (this repo): <https://github.com/mini-kep/intro>
- Parsers:
  - [master repo for parser templating](https://github.com/mini-kep/parser-template) (under development)  
  - ```kep```: <https://github.com/mini-kep/parser-rosstat-kep> [![](https://travis-ci.org/mini-kep/parser-rosstat-kep.svg?branch=master)](https://travis-ci.org/mini-kep/parser-rosstat-kep)
- Database: <https://github.com/mini-kep/db/> (under development)
- Front end app: <https://github.com/mini-kep/frontend-app> [![Build Status](https://travis-ci.org/mini-kep/frontend-app.svg?branch=master)](https://travis-ci.org/mini-kep/frontend-app)

All pipeline [mocked here](https://github.com/mini-kep/db/tree/master/doc). 

# Dev notes

#### naming convention: 
   - used in 'kep' parser specification extensively
   - descrition/tree dictionaries:
      - [ ] varname-description
      - [ ] units-description 
      - [ ] section-varname    

#### parsers: migrate after templating
  - [ ] make list of parsers 
  - [ ] common parser interface 
  - [ ] common components (eg. download)
  - [ ] description template (json to markdown)
  - [ ] API keys(?)
  - [ ] [migrate parsers to github organisation](https://github.com/mini-kep/intro/issues/4) 


#### scheduler: 
   - discussed, does not exist
   - needs parser json (2) + db (3) + scheduling rules 

#### charts

> making standartised charts for fronends and user notebooks and injecting them across project


#### dataset basis

> what is the minimum number of variables to keep in basis to reproduce end-user dataset (involves levelising rates and 
> separating nominal and real variables), abstracting form rounding error and annual revisions; will be an input to seasonal 
> adjustment and API interface planning, see below

#### seasonal adjustment
> explore techniques and establish own procedure + variable naming + point of injection in dataflow 


#### github org migration

See [issues](https://github.com/mini-kep/intro/issues?utf8=%E2%9C%93&q=is%3Aissue%20is%3Aopen%20migration)
about moving various repos to here, adjusting frontend app and urls in access examples. 

Other notes
===========

- *'maas'* - forecasting model as a service (experimental)

- This pipeline may also apply to other countries macroeconomic data, or other kinds datasets (eg firm-level data, banking statistics). 
