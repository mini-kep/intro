Introduction
============

```mini-kep``` is a small ETL (extract, transform, load) framework for 
Russian and global macroeconomic time series data with public end-user API.

It is inspired by [St Louis FRED](https://fred.stlouisfed.org) and 
[Data Science Cookiecutter](https://drivendata.github.io/cookiecutter-data-science)
and aims to provide timely machine-readable data for reproducible analysis 
in (macro)economics.

Please [fill a poll about economics data sources](https://goo.gl/2wY43R)
to support our case.  

Project links
=============

Data browser: <http://macrodash.herokuapp.com>

Key repositories:
- [parsers](https://github.com/mini-kep/parsers)
- [database](https://github.com/mini-kep/db)
- [frontend](https://github.com/mini-kep/frontend-dash)
- [user charts](https://github.com/mini-kep/user-charts)

Documentation: <https://mini-kep.github.io/documentation>

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

Project map 
===========

![image](https://user-images.githubusercontent.com/9265326/32406266-57004848-c186-11e7-951e-2d40b4a3ffda.png)

See also
========
- [development notes](DEV.md) 
- [changelog](changelog.md)
- [testing guidelines](https://github.com/mini-kep/intro/blob/master/testing_guidelines/README.md)
