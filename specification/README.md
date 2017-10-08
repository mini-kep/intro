Introduction 
============

```mini-kep``` is a small ETL (extract, transform, load) framework for 
macroeconomic data with public end-user API.

Dataflow 
========
```mini-kep``` organises a data pipeline from sources 
(static files in internet and public APIs) to database to end-user API. The pipeline is the following:

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

Finished spec:
- [database layer](database.md)

Under construction:
- [usercase](usercase.md)
- [parsers](parsers.md)
- [custom API](custom_API.md)

Will wait:
- [scheduler](scheduler.md)
- [frontpage](frontpage.md)
- [django_app.md](django_app.md) - dormant

For discussion:
- [data model and namespace](datamodel_and_namespace.md)
