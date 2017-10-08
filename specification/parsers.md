Data sources and parsers
------------------------

Data sources are static files (Word, PDF, html) and some open APIs. Parser is the python code performing requests and emitting datapoints. 

[parser-rosstat-kep](https://github.com/mini-kep/parser-rosstat-kep) supplies most time series. It is supplemented by daily ruble exchange rate from Bank of Russia and oil prices from EIA and some others.

Aggratation of parser data is made at [parsers/runner.py](https://github.com/mini-kep/parsers/blob/master/parsers/runner.py)

[parser-rosstat-kep](https://github.com/mini-kep/parser-rosstat-kep):
[![](https://travis-ci.org/mini-kep/parser-rosstat-kep.svg?branch=master)](https://travis-ci.org/mini-kep/parser-rosstat-kep) 
[![](https://codecov.io/gh/mini-kep/parser-rosstat-kep/branch/master/graphs/badge.svg)](https://codecov.io/gh/mini-kep/parser-rosstat-kep)

[parsers](https://github.com/mini-kep/parsers):
[![](https://travis-ci.org/mini-kep/parsers.svg?branch=master)](https://travis-ci.org/mini-kep/parsers)
[![](https://codecov.io/gh/mini-kep/parsers/branch/master/graphs/badge.svg)](https://codecov.io/gh/mini-kep/parsers) 

