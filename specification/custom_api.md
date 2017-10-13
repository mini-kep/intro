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

> this is a duplicte, will need to reference it to source

> TODO: update with https://github.com/mini-kep/frontend-app/blob/master/apps/templates/home.md

```python
# monthly consumer inflation time series for Russia in 2015-2017
# rog is 'rate of growth'
df = pd.read_json("http://mini-kep.herokuapp.com/ru/series/CPI/m/rog/2015/2017")

# get daily oil prices for Brent, same period
df = pd.read_json("http://mini-kep.herokuapp.com/oil/series/BRENT/d/2015/2017") 

```

The data provided by custom API must be readable by ```pd.read_json()```

In order to ensure data integrity, some options need to be enabled in the
```pd.read_json``` command on the client side. This can be accomplished by
wrapping the function call in a partial, as follows:

> TODO: partial is ok, can be a solution 

```python
from functools import partial
read_csv = partial(pd.read_csv, converters={0: pd.to_datetime}, index_col=0)
read_json = partial(pd.read_json, precise_float=True, orient='split')
```

URL format
==========

> this is a duplicte, will need to reference it to source

```
{domain}/series/{varname}/{freq}/{?suffix}/{?start}/{?end}/{?finaliser} 

   ? - indicates optional parameter
```
       
`{domain}` is reserved, future use: 'all', 'ru', 'oil', 'ru:bank', 'ru:77'

`{varname}` is GDP, GOODS_EXPORT, BRENT (capital letters with underscores)

`{freq}` is any of:  
- a (annual)
- q (quarterly)
- m (monthly)
- w (weekly)
- d (daily)

`{?suffix}` may be: 
- unit of measurement (unit):
    - example: bln_rub, bln_usd, tkm
     
- rate of change for real variable (rate):
    - rog - change to previous period
    - yoy - change to year ago
    - base - base index
     
- aggregation command (agg): 
    - eop - end of period
    - avg - average
    
> TODO should we make a link to docstring?    

Examples:

```
oil/series/BRENT/m/eop/2015/2017/csv
ru/series/EXPORT_GOODS/m/bln_rub
```

What next
---------

What developpers are about to do next

Changelog
---------

Big events / chnages
