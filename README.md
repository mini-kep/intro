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

We assume an end user has some experience with data from FRED or quandl and for his work he wants:

- a clean dataset with latest data from different sources
- browse what data is available
- read this data on a local machine:
   - as pd.DataFrame 
   - as R dataframe  
- quickly draw some charts like one below: 

[![](http://datachart.cc/images/rub_oil.png)](http://datachart.cc/)

More on user case [here](specification/usercase.md)

Read next
=========

- [Specification pages](specification/readme.md)
- [Development notes](DEV.md) 
- [Changelog](changelog.md)
- [New user checklist](wiki/New-user-checklist)

