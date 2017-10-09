Overview
========


Custom API is a simplified interface for end-user queries. It is done in 'reddit' style: a long URL with slashes.

```
# monthly consumer inflation time series for Russia in 2015-2017
# 
df = pd.read_json("http://mini-kep.herokuapp.com/ru/series/CPI/m/rog/2015/2017")

# get daily oil prices for Brent, same period
df = pd.read_json("http://mini-kep.herokuapp.com/oil/series/BRENT/d/2015/2017") 

```

The intent is to allow:
- intuitive construction of URL for user
- shorter notation than standard database API GET method 
- get similar data for different countries / regions just by changing little part of URL

The data provided by custom API must be readable by ```pd.read_json()```


URL format
==========

```
<domain>/series/<varname>/<frequency>/<?suffix>/<?start_year>/<?end_year>/<?finaliser>

   <suffix> is either unit of measurement or rate of change or aggregation command 

   ? - indicates optional parameter
```


Functionality
=============

1. **Translate URL:** custom API must translate long url into parameters to database API GET call.
2. **Provide pandas-readable data**: there should be database API GET method that returns json readable by ```pd.read_json()```.


Implementation 
===============

1. Custom API design was originally discussed [here](https://github.com/mini-kep/frontend-app/issues/8). 
   The result of the discussion is url format above. In discussion there are certain extras for future features.

2. Initial veriosn of custom API is implemented as a part of fronetnd app at <https://github.com/mini-kep/frontend-app/blob/master/apps/views/time_series.py>. It is responsible for translating URLs into parameter dictionaries.

Try and click: 
 - <http://mini-kep.herokuapp.com/ru/series/CPI/m/rog/2017>
 - <http://mini-kep.herokuapp.com/oil/series/BRENT/d/2000/2005>
 
3. New implemtation of URL translation is at <https://github.com/mini-kep/helpers/issues/3>  
   and <https://github.com/mini-kep/helpers/blob/master/custom_api.py>.
   
4. We do not have conversion of existing GET output to pandas-readable format yet. May consult prototype at 
   <https://github.com/mini-kep/intro/blob/master/pipeline/pipeline.py> on how this may be done.
   
   
   
