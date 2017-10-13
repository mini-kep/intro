Overview
========

Custom API is a simplified interface for end-user queries. 
The syntax for it is long URL with slashes like below

```
http://mini-kep.herokuapp.com/ru/series/CPI/m/rog/2015/2017

```
The intent of cuspom API is to allow:
1. intuitive construction of URL for user
2. shorter notation than standard database API GET method 
3. get similar data for different countries / regions just by changing little part of URL


Usage example
============

*TODO same as in http://mini-kep.herokuapp.com* frontpage


```
# monthly consumer inflation time series for Russia in 2015-2017
# rog is 'rate of growth'
df = pd.read_json("http://mini-kep.herokuapp.com/ru/series/CPI/m/rog/2015/2017")

# get daily oil prices for Brent, same period
df = pd.read_json("http://mini-kep.herokuapp.com/oil/series/BRENT/d/2015/2017") 

```

The data provided by custom API must be readable by ```pd.read_json()```


URL format
==========


```
<domain>/series/<varname>/<frequency>/<?suffix>/<?start_year>/<?end_year>/<?finaliser>

   ? - indicates optional parameter
```

```<suffix>``` can be unit of measurement or rate of change or aggregation command



Functionality
=============

#### 1. Translate URL

Custom API must translate long url into parameters to database API GET call. Done at:
   - <https://github.com/mini-kep/frontend-app/blob/master/apps/views/time_series.py>
   - <https://github.com/mini-kep/helpers/blob/master/custom_api.py> (newer)

#### 2. Provide pandas-readable data

Database GET method currently returns a json with a list of datapoints, and this data should be converted
into json readable by ```pd.read_json()```.

Such conversion is done at <https://github.com/mini-kep/intro/blob/master/pipeline/pipeline.py> .


Implementation 
===============

1. Custom API design was originally discussed [here](https://github.com/mini-kep/frontend-app/issues/8) and [here](https://github.com/mini-kep/intro/issues/12).
   The result of the discussion is url format above. In discussion there are certain extras for future features.

2. Initial veriosn of custom API is implemented as a part of fronetnd app at <https://github.com/mini-kep/frontend-app/blob/master/apps/views/time_series.py>. It is responsible for translating URLs into parameter dictionaries. Try and click: 
   - <http://mini-kep.herokuapp.com/ru/series/CPI/m/rog/2017>
   - <http://mini-kep.herokuapp.com/oil/series/BRENT/d/2000/2005>
 
3. New implemtation of URL translation is at <https://github.com/mini-kep/helpers/issues/3>  
   and <https://github.com/mini-kep/helpers/blob/master/custom_api.py>.
   
4. We do not have conversion of existing GET output to pandas-readable format yet. May consult prototype at 
   <https://github.com/mini-kep/intro/blob/master/pipeline/pipeline.py> on how this may be done.
   
   
Uncertainties 
=============

- ```<domain>``` may conflict with some API prefixes
- custom API should migrate to ```db``` instead of ```frontend-app```   


TODO
====

- [ ] in database we need a GET method to provide pandas-readable json
- [ ] newer url decomposition
- [ ] mount endpoint at frontend app (?)
- [ ] mount endpoint at db app (?)
- [ ] testing


