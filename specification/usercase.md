
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


We assume end-user is well-versed in FRED or quandl and for Russian or custom statistics he/she wants:

- a clean dataset with latest data from different sources
- browse what data is available
- read this data on a local machine:
   - as pd.DataFrame 
   - as R dataframe  
- quickly draw some charts like one below: 

[![](http://datachart.cc/images/rub_oil.png)](http://datachart.cc/)