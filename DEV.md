Critical path
-------------

0. db api with csv output -> use cases

1. parser specification -> more data -> richer use cases

2. use cases discussion / dessemination


Advanced usage
--------------

Services based on mini-kep API: 

- PDF handout charts  
- datasets/presets
- forcasts as a service (via API)
- FB posts with charts
  
  
Tasks - higher priority
-----------------------

#### use cases:
   - [ ] case thesis

#### custom API:
   - [ ] as in <https://github.com/mini-kep/helpers/issues/3>

#### parsers
   - [ ] finished testing existing parsers
   - [ ] parser specification
   - [ ] isep parser

#### new home for specification
   - [x] all specs and drafts found at intro/specification (EP)
   - [ ] cleaner documentation 

#### db layer
   - [ ] smaller test dataset for db API
   - [ ] db flask tests extended
   - [ ] add new methods needed - as in issue <https://github.com/mini-kep/db/issues/8>

Tasks - lower priority
-----------------------

#### cross-functional
   - [ ] consistency checks as in kep parser

#### infrastructure   
   - [ ] infrastructure - minikep.cc domain
   
#### frontend app
   - [ ] fronend should have indicator listing
   - [ ] fronend should have indicator homepages
   
#### scheduler    
   - [ ] need a simple scheduler to update info: the task to run + cron-like invoker

#### other:
   - [ ] started parser-rosstat-isep
   - [ ] maintainer found for 806 parser   

Development ideas
-----------------

Use cases:
- [ ] gdp components
- [ ] inflation
- [ ] fx
- [ ] bank provisions model
  
Advanced content:
- [ ] seasonally adjusted time series as ```/sa:<method>``` 
- [ ] forecasts as ```/forecast:<version>/2025```

New APIs:
- [ ] dataset API - load several time series
- [ ] Excel files delivered by ```xl``` finaliser
- [ ] chart API with ```spline``` and ```chart``` finaliser

Viewing:
- make a dashboard for macroeconomic indicators 
- view a dashboard on a smartphone / get notifications 
