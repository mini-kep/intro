Introduction 
============

```mini-kep``` is a small ETL (extract, transform, load) framework for 
macroeconomic data with public end-user API.

End-user API calls should be like:
  
```python 

# monthly average Brent oil prices starting 2000 to present 
brent = pd.read_json('http://minikep.cc/oil/series/BRENT/m/avg/2000')

# monthly average Russian rouble exchange rate, same period
er = pd.read_json('http://minikep.cc/ru/series/USDRUR/m/avg/2000')

# monthly consumer inflation in different countries in 2017
# rog = rate of growth 
cpi_ru = pd.read_json('http://minikep.cc/ru/series/CPI/m/rog/2017')
cpi_us = pd.read_json('http://minikep.cc/us/series/CPI/m/rog/2017')

```

Dataflow 
========
```mini-kep``` organises a data pipeline from sources 
(static files in internet and public APIs) to database to end-user API.
With this API the user download data шт R/pandas as dataframes.

The pipeline is the following:

 1. data sources and parsers 
 2. *scheduler*
 3. database and db API
 4. *custom API*
 5. *user cases* 
 
Elements in progress are in italic.

Frontpage
=========

Frontpage is a stand-alone flask app that is used to:
- relay some existing data in experimental mode 
- make a list of indicators available in ```mini-kep``` database
- show individual indicators homepages with charts, latest values 
  and instructions for download.
  
Read more at [specification](frontpage.md)  

Specifications
==============

In due course of work following specifications are used:
- parsers
- database layer
- custom API
- frontpage

For discussion:
- data model and namespace