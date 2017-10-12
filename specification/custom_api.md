Overview
========

Custom API is a simplified interface for end-user queries. It is done as a long URL with slashes (similar to a 'reddit' style).

```python
# monthly consumer inflation time series for Russia in 2015-2017
# rog is 'rate of growth'
df = pd.read_json("http://mini-kep.herokuapp.com/ru/series/CPI/m/rog/2015/2017")

# get daily oil prices for Brent, same period
df = pd.read_json("http://mini-kep.herokuapp.com/oil/series/BRENT/d/2015/2017") 

```

The intent is to allow:
- intuitive construction of URL for user
- shorter notation than standard database API GET method 
- get similar data for different countries / regions just by changing little part of URL

The data provided by custom API must be readable by ```pd.read_json()```

In order to ensure data integrity, some options need to be enabled in the
```pd.read_json``` command on the client side. This can be accomplished by
wrapping the function call in a partial, as follows:

```python
from functools import partial
read_csv = partial(pd.read_csv, converters={0: pd.to_datetime}, index_col=0)
read_json = partial(pd.read_json, precise_float=True, orient='split')
```


URL format
==========

```
{domain}/series/{varname}/{freq}/{?suffix}/{?start}/{?end}/{?finaliser} 

   ? - indicates optional parameter
```

We can relax restrictions of suffix and just query ```name:varname_suffix``` without prior checks.

#### Tokens:         
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


#### Examples:
```
oil/series/BRENT/m/eop/2015/2017/csv
ru/series/EXPORT_GOODS/m/bln_rub
```
