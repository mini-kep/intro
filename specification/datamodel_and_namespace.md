Datamodel and enduser API
=========================

The idea of mini-kep project is to allow simple retrieval of Russian macroeconomic data 
into python pandas and R, using an intuitive notation about variable naming and 
modifiation.

We want an end-user to make a call like this to get qurterly nominal GDP and 
real GDP growht rate: 

```python

gdp_nominal = pd.read_json('https://mini-kep.herokuapp.com/ru/series/GDP/q')
gdp_real_growth_rate = pd.read_json('https://mini-kep.herokuapp.com/ru/series/GDP/q/rog')

``` 

```rog``` is rate of growth, real growth rate to previous period 

Daily oil prices and exchange rates can be retrieved as: 

```python

brent = pd.read_json('https://mini-kep.herokuapp.com/oil/series/BRENT/d')
#exchange rate
er = pd.read_json('https://mini-kep.herokuapp.com/ru/series/USDRUR/d')
```

As of now the API frontend just shows how flask decodes long URL into a dict/json. You can click and see:

- <https://mini-kep.herokuapp.com/ru/series/BRENT/m>
- <https://mini-kep.herokuapp.com/ru/series/BRENT/m/eop/2015/2016/csv>
- <https://mini-kep.herokuapp.com/ru/series/GDP/q/rog>

The URL/API is styled around:
- ```https://mini-kep.herokuapp.com/<domain>/series/<VARNAME>/<frequency>``` - mandatory part
- ```<mandatory part>/<modifier | aggregator>/<start_year>/<end_year>/<finaliser>``` - optional part

The functionaly described not implemented yet, but hopefully soon be. For this to happen:
- at [parser-template](https://github.com/mini-kep/parser-template) we are working on importing parsing results (kep+exchange rate+oil) as dictionaries with datapoints 
- at [db](https://github.com/mini-kep/db) the datapoints are to be stored in a database   
- [the frontend app](https://github.com/mini-kep/frontend-app) should be able to query the database and provide real data for 
  calls above.
  
An important link that I propose to explore is what our datamodel for 
the macroeconomic data and how to make good API documentation and prototype. 
As for API the tricky part is making a 'reddit' style slashed API which 
assumes default values for some cases + some token combinations are invalid.

More to follow:
- how we can get the data extracted (getter.py) + what is done with other parsers
- naming convention in 'parser-rosstat-kep'
- questions about data consistency and checks performed
- 'true dataset' (affests API design and verification)
- API blueprint
- translate API call to database call (this should be sample code with a lot of test)
- API v.0.1 vs features for the future

Suggested reading/code
======================

- ```read_csv()```: 
   - [getter.py](https://github.com/mini-kep/parser-rosstat-kep/blob/master/src/getter.py)
   - [parser-rosstat-kep readme](https://github.com/mini-kep/parser-rosstat-kep/blob/master/README.md#how-do-i-download-macroeconomic-indicators-from-here)
   - [app frontpage code](http://mini-kep.herokuapp.com/)

> This is a data access function used across the project to read the output as dataframes from stable URLs
> In end-user API the import function will be  ```pd.read_json``` as it will allow to bypass time index transformation:

```
annual_CPI_rog = pd.read_json('http://mini-kep.herokuapp.com/ru/series/CPI/a/rog')
```

- [dataframe consistency](https://github.com/mini-kep/parser-rosstat-kep/blob/master/src/utils/df_check.py):

> This module checks consistency of the results in the database. In particular, the monthly frequency 
> dataframes are aggregated to an annual frequency, and checked against the published annual results. 
> More functions checking for consistency in other frequencies can be added (eg monthly to quarterly, quarterly to annual)
> We found some inconsistencies were reported data on annual level is different that the log-sum on monthly rates,
> even controlling for rounding error.

- [API design issue](https://github.com/mini-kep/frontend-app/issues/8)

> From here we need to extract the text on data rules and API documentation 

Glossary
========

- data model
- true dataset
- reported dataset
- enduser API
