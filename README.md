Why another database for macroeconomic data?
============================================

- Machine-readable datafeeds for economic data are growing (FRED, quandl, World Bank, EIA among others), yet some data is left behind
- Russian macroeconomic statistics seems very fragmented (Word, Excel) and this is a roadblock to cool reproducible analysis and reliable inputs for business planning, also escalates costs of modelling/forecasting      
- ```mini-kep``` aims to fill this gap by providing public API for macroeconomic data and examples of economic research/business planning/marketing problems solved using python pandas or R.
- May also apply to other countries macroeconomic data, or other (microeconomic / 'real world') datasets 

Data pipeline / workflow 
========================

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
   - html content for veiwing
   - end-user API(s)

5. end-user examples/solutions
   - data access examples for end-user API
   - charting macroeconimic data
   - models in jupiter notebooks
   - *'maas'* - forecasting model as a service (experimental)


What is happing now in the project
==================================

#### 11-09-2017:

- [ ] **dataset basis** - what is the minimum number of variables to keep in basis to reproduce end-user dataset (involves levelising rates and separating nominal and real variables), abstracting form rounding error and annual revisions; will be an input to seasonal adjustment and API interface planning, see below

- [ ] **seasonal adjustment**, or *sa* - explore techniques and establish own procedure (and variable naming + point of injection in dataflow) to 

- [ ] **variable descriptions** - need to tell what ```GDP_yoy``` means. Will involve varname-description, units-description and section-varname dictionaries. 

- [ ] **charts** - making standartised charts for fronends and user notebooks and injecting them across project

- [ ] **database** - making component (3) for the project based, with unit tests from a start. Doing component (2) after/with that. 

- [ ] **github org migration** - moving various repos to here, adjusting frontend app and urls in access examples

TODO (EP): provide links to issues/repos 


