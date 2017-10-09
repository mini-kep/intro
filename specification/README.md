Introduction 
============

```mini-kep``` is a small ETL (extract, transform, load) framework for 
macroeconomic data with public end-user API.

Dataflow 
========
```mini-kep``` organises a data pipeline from sources 
(static files in internet and public APIs) to database to end-user API. 

The data pipeline is the following:

 1. [data sources and parsers](https://github.com/mini-kep/parsers) 
 2. *scheduler (not implemented)*
 3. [database and db API](https://github.com/mini-kep/db)
 4. *custom API (draft)*
 5. *user cases (draft)* 

Pipeline is illustrated by [pipeline.py](https://github.com/mini-kep/intro/blob/master/pipeline/pipeline.py)
 
Specifications
==============

Finished spec:
- [database layer](database.md)

Under construction:
- [parsers](parsers.md)
- [custom API](custom_api.md)
- [usercase](usercase.md)

On hold:
- [scheduler](scheduler.md)
- [frontend](frontend.md)
- [django_app.md](django_app.md)

For discussion:
- [data model and namespace](datamodel_and_namespace.md)
