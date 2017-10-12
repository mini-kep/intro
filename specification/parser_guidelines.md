Parsers Guidelines
==================
Parsers in ```mini-kep``` are used to fetch data from various sources as raw data in Json, XML and csv formats, parse those data and yield them in common formated output.

Introduction
------------
Parsers gudelines provide detailed information how parsers are constructed. This guidelines should provide manual to speed up new parses development

Checklist
---------
1. Define Source
2. Fetch RAW content from source
3. Parse fetched content
4. Yield content in desired format

Define Source
-------------
When defining source for fetching raw data, one needs to take into consideration as part of URL construction, timeframe or frequency often needs to be incorporated.

Sources for fetching up RAW data can be:
1. public API calls
2. public ASP calls
3. public CSV files
4. ...

Fetch RAW content from source
-----------------------------
To Fetch Raw content from websource ```fetch()``` generic method is available in parsers repo ```parsers/getter/util.py```

Parse fetched content
---------------------
Dates, datapoint names and prices need to be parsed from fetched content. Parsing is done with third party libraries listed below based on the content type:
- XML : BeautifulSoup, xml.etree.ElementTree
- CSV : Pandas, Numpy
- JSON : json

utilities to format dates and prices are available in ```parsers/getter/util.py``` > ```format_date()``` and ```format_value()```

Yield content in desired format
-------------------------------
Parsed values need to be yielded from particular parses in format below:
```
yield {'date': date,
          'freq': freq,
          'name': name,
          'value': price}
```
Contributors
------------
[Jaroslav Vojtek](https://www.upwork.com/freelancers/~01eeba06021f7e72ef?viewMode=1)
