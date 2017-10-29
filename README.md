Introduction
============

```mini-kep``` is a small ETL (extract, transform, load) framework for 
Russian and global macroeconomic time series data with public end-user API.

It is inspired by [St Louis FRED](https://fred.stlouisfed.org) and 
[Data Science Cookiecutter](https://drivendata.github.io/cookiecutter-data-science)
and aims to provide open, timely, machine-readable data for reproducible 
analysis in economics.

To support our case please 
[fill a poll about your usage of economics datasources](https://goo.gl/2wY43R).  


Motivation: why another database for macroeconomic data?
========================================================
 
- Machine-readable datafeeds for economic data are growing (
  [FRED](https://research.stlouisfed.org/docs/api/fred/), 
  [quandl](https://blog.quandl.com/api-for-economic-data), 
  [OECD](https://data.oecd.org/api), 
  [World Bank](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589), 
  [EIA](https://www.eia.gov/opendata/)).

- However, some data is still left in the dark. Russian macroeconomic statistics seems very 
  fragmented (HTML, Word, Excel are common dessimination formats). 
  This is a roadblock to reproducible analysis as dirty data escalates costs of model maintenance.      

- ```mini-kep``` aims to remove this roadblock by providing 
  [public API for Russian macroeconomic data](http://mini-kep.herokuapp.com/) 
  and examples of economic research/business planning/marketing problems 
  solved in python pandas or R.
  
How can I access the data? 
==========================

```python 
import pandas as pd

def read_ts(source_url):
	"""Read pandas time series from *source_url*."""
	return pd.read_csv(source_url, 
                       converters={0: pd.to_datetime}, 
                       index_col=0,
                       squeeze=True)

er = read_ts('http://minikep-db.herokuapp.com/ru/series/USDRUR_CB/d/2017')
assert er['2017-09-28'] == 58.01022
```  
  
Documentation 
=============

See [project documentaion](https://mini-kep.github.io/documentation).

Project map 
===========

![](https://user-images.githubusercontent.com/9265326/32145726-59b4cec6-bcde-11e7-8d58-ef67f4224411.png)


See also
========
- [development notes](DEV.md) 
- [changelog](changelog.md)
- [testing guidelines](https://github.com/mini-kep/intro/blob/master/testing_guidelines/README.md).
