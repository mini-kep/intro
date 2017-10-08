(4) Custom API 
--------------
Custom API simplified interface for end-user queries. 

Custom API endpoint is a long URL at a frontend flask app that translates this URL to a database query and supplies data as json readable by ```pd.read_json()```

Example (returns its parameters, not implemented):
- <http://mini-kep.herokuapp.com/ru/series/BRENT/m/eop/2017>

