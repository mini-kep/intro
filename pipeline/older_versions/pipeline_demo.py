# -*- coding: utf-8 -*-

import json
from pprint import pprint
import time


import pandas as pd

d = {'RUR_EUR_eop': pd.Series([48.1, 49.35, 49.05, 49.51, 47.27, 45.83, 47.9, 48.63, 49.95, 54.64, 61.41, 68.34, 78.11, 68.69, 63.37, 56.81, 58.01, 61.52, 64.65, 75.05, 74.58, 70.75, 70.39, 79.7]), 
     'CPI_rog': pd.Series([100.6, 100.7, 101.0, 100.9, 100.9, 100.6, 100.5, 100.2, 100.7, 100.8, 101.3, 102.6, 103.9, 102.2, 101.2, 100.5, 100.4, 100.2, 100.8, 100.4, 100.6, 100.7, 100.8, 100.8])}
ix = pd.date_range(start='2014-01-01', periods=12*2, freq='M')


# 0. Here is something a user wants, Jane is working with dfm DataFrame  

dfm = pd.DataFrame(d).set_index(ix)

# 1. parser jobs

# 1.1 parser1 parsed something and is ready to provide the data

to_serialise = json.loads(dfm.to_json(None,'index', date_format='iso'))

observations = [dict(date=k.replace('T00:00:00.000Z',''),
                     freq='m',
                     varname = a,
                     value = b) 
                for k, v in to_serialise.items() 
                for a, b in v.items()]

parcer_output1 = json.dumps(observations, indent=4)
print()
print("This goes from parser 1 to database")
print("====================================")
print(parcer_output1)

# 1.2 parser2 parsed something else and is ready to provide the data too
#     it is likely to be different variables, but I'll show same var at different frequency

observations = [
    {"date": "2014-03-31", "freq": "q", 
     "varname": "CPI_rog", "value": 102.3}
    ]

parcer_output2 = json.dumps(observations, indent=4)

print()
print("This goes from parser 2 to database")
print("===================================")
print(parcer_output2)



# 2. the database accepted 1.1 and 1.2 this and stores the data in whichever 
#    is most appropriate format 

# ...

# 3. the user sends a query to the database

user_query = dict(varnames=['CPI_rog', 'RUR_EUR_eop'],
                  freq='m',
                  start='2014-01', # optional
                  end='2015-12' # optional
                  )

print()
print("User query")
print("==========")
pprint(user_query)



# 3. based on a query, the database will send this json to the user

# we use dfm.to_json() to show, but the real json will be constructed from the database  
# dfm will not be available at this time
json_query_result = dfm.to_json() 
print()
print("App response to query: json with epoch timestamps")
print("=================================================")
print("This format is default input \nto user reader function pd.read_json()")
pprint(json.loads(json_query_result))


#4. the user accepts json and renders it locally to dataframe type  
dfm_at_user = pd.read_json(json_query_result)
print()
print("User's local dataframe")
print("======================")
print(dfm_at_user)
flag = dfm_at_user.equals(dfm) 
assert dfm_at_user.equals(dfm) 


print("Identical to source data:", flag)


# concerns:

# 1. when quering for parser result must decide which dates are newest
#    must not ask for all of data from long ago
    
   
# 2. namespaces can be useful, eg ru/CPI_rog, us/CPI_rog, eu/CPI_rog    
#    can map parser names to namespaces


# notes:
    
# even with one time series, read_jsom retrurns Dataframe, not Series
f = """{"CPI_rog": {"1391126400000": 100.6, 
             "1393545600000": 100.7, 
             "1396224000000": 101.0,
             }}"""
assert isinstance(pd.read_json(f), pd.DataFrame)

# converting epoch
epoch = "1451520000000"
assert "2015-12-31" == time.strftime('%Y-%m-%d', 
                       time.localtime(int(epoch) / 10 ** 3))


# can use this learn about 'orient' paramater 
#for orient in ('split','records','index','columns','values'):
#    print()
#    this_json = dfm.to_json(None, orient)
#    size = len(str(this_json))
#    print(orient, size)
#    print(this_json)
