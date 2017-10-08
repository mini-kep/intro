Introduction 
============

```mini-kep``` is a small ETL (extract, transform, load) framework for 
macroeconomic data with public end-user API.

Dataflow 
========
```mini-kep``` organises a data pipeline from sources 
(static files in internet and public APIs) to database to end-user API.
With this API the user download data шт R/pandas as dataframes.

The pipeline is the following:

 1. [data sources and parsers](https://github.com/mini-kep/) 
 2. *scheduler (not implemented)*
 3. [database and db API](https://github.com/mini-kep/db)
 4. *custom API (draft)*
 5. *user cases (draft)* 

Pipeline is illustrated by [pipeline.py](https://github.com/mini-kep/intro/blob/master/pipeline/pipeline.py)
 
Frontpage
=========

Frontpage is a stand-alone flask app that is used to:
- relay some existing data in experimental mode 
- make a list of indicators available in ```mini-kep``` database
- show individual indicators homepages with charts, latest values 
  and instructions for download.
  
Read more at [specification](frontpage.md)  

Specifications
==============

In due course of work we used follwoing specs:
- [database layer](database.md)

Under construction:
- [parsers](parsers.md)
- [custom API](custom_API.md)

Will wait:
- [usercase](usercase.md)
- [scheduler](scheduler.md)
- [frontpage](frontpage.md)

For discussion:
- [data model and namespace](datamodel_and_namespace.md)

Dormant:
- [django_app.md](django_app.md)