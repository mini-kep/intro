Overview
========

Custom API is a simplified interface for end-user queries from database. 
It uses long URL with slashes and no other parameters.

This call: 

```http://mini-kep.herokuapp.com/ru/series/CPI/m/rog/2015/2017```

will return same data as:

```https://minikep-db.herokuapp.com/api/datapoints?name=CPI_rog&freq=m&start_date=2015-01-01&end_date=2017-12-31```

The intent of custom API is to allow:
1. intuitive construction of URL for user
2. shorter notation than standard database API GET method 
3. get similar data for different countries / regions just by changing little part of URL, for example: 
   - ```ru/series/CPI/m/2017``` is nationwide inflation for Russia 
   - ```ru:77/series/CPI/m/2017``` is inflation for Moscow region (from [here](http://www.gks.ru/bgd/regl/b16_17/IssWWW.exe/Stg/10-2-1.xls))  
   - ```kz/series/CPI/m/2017``` is same national indicator for Kazakhstan.


How is it implemented
=====================

> ideas on how it is implemented - with respect to flask 

> or suggestions on implementation 

Custom API is mounted at <http://mini-kep.herokuapp.com/>, see below for details. 

> todo: where the code is 

> todo: where the data is 

Client side code
================

In order to ensure data integrity, some additional parameters need to be specified when importing data with ```pd.read_json``` or ```pd.read_csv```.
See [here](custom_api_client_side_code.py) for examples on how to load data into a dataframe.

URL format
==========

Some more examples illustrating the format of the URLs;
```
oil/series/BRENT/m/eop/2015/2017/csv
ru/series/EXPORT_GOODS/m/bln_rub
```
For further details, refer to the [docstring](https://github.com/mini-kep/helpers/blob/master/custom_api/custom_api.py#L1-L46) in the custom_api.py file.

What next
---------

What developers are about to do next

Changelog
---------

Big events / changes
