(4) Custom API 
--------------
Custom API simplified interface for end-user queries. 

Custom API endpoint is a long URL at a frontend flask app that translates this URL to a database query and supplies data as json readable by ```pd.read_json()```

Example (returns its parameters, not implemented):
- <http://mini-kep.herokuapp.com/ru/series/BRENT/m/eop/2017>

##  Custom end user API

We expect end user will call like below run: 
```python 

# get monthly consumer inflation time series for Russia in 2017
df = pd.read_json("http://mini-kep.herokuapp.com/ru/series/CPI/m/rog/2017")

# get daily oil prices for Brent between 2000 and 2005
df = pd.read_json("http://mini-kep.herokuapp.com/oil/series/BRENT/d/2000/2005") 

```

Custom API is discussed here: <https://github.com/mini-kep/frontend-app/issues/8>

Initial version of custom API is here: <https://github.com/mini-kep/frontend-app/blob/master/apps/views/time_series.py>

The calls to custom URLs now return parameter dictionaries, try and click: 
 - <http://mini-kep.herokuapp.com/ru/series/CPI/m/rog/2017>
 - <http://mini-kep.herokuapp.com/oil/series/BRENT/d/2000/2005>
 
 
> for my understanding, so there's two possible task for now first is work on https://github.com/mini-kep/helpers/issues/3 and the second one is write specification in https://github.com/mini-kep/intro/blob/master/specification/custom_api.md. am I missing something?

