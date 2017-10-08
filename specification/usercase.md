User case notes
================

Easy data access
----------------

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

We assume end-user is familiar with FRED or quandl and uses R or pandas for work. 

For Russian or some other custom statistics he wants:

- a clean dataset with latest data from different sources
- browse what data is available
- read this data on a local machine:
   - as pd.DataFrame 
   - as R dataframe  
- quickly draw some charts like one below: 

[![](http://datachart.cc/images/rub_oil.png)](http://datachart.cc/)


Advanced usage
--------------

- services based on mini-kep API 
- handout charts  


Notebooks and code
------------------

Use cases  are sample visualisations and models relying on data from custom API.

There is a [repo for use cases](https://github.com/mini-kep/user-charts), but it is practically empty, as I'm busy constructing the data pipeline.

The use cases may resemble [datachart.cc](http://datachart.cc/)  
or [datalab](https://github.com/epogrebnyak/data-lab)
or [viz-demo](https://github.com/epogrebnyak/viz_demo)


