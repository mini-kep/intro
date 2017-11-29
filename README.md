[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/mini-kep/Lobby)

Goal
====

The project goal is to provide open, timely, machine-readable data for reproducible 
(macro)economic research.

Introduction
============

```mini-kep``` is a collection of data parsers + a database with public end-user API 
that delivers macroeconomic time series.

The current dataset has Russian and some global macroeconomic data. It is available through:
- [data browser](http://macrodash.herokuapp.com)
- [variable listing](https://github.com/mini-kep/db/blob/master/doc/listing.md)
- [pandas access code](https://github.com/mini-kep/user-charts/blob/master/access.py) 

Main code repositories are:
- [parsers](https://github.com/mini-kep/parsers)
- [database](https://github.com/mini-kep/db)
- [data browser](https://github.com/mini-kep/frontend-dash)  

If you work with economic time series, please fill our poll about [data sources](https://goo.gl/2wY43R)
to help us understand user needs.

The project idea is heavily influenced by:
- [St Louis FRED](https://fred.stlouisfed.org) 
- [Data Science Cookiecutter](https://drivendata.github.io/cookiecutter-data-science)
 

User cases 
==========

[This repo](https://github.com/mini-kep/user-charts) has notebooks and charts using the dataset.
Feel free to contibute your economic analysis task or idea for it [by gitter](https://gitter.im/mini-kep/Lobby).

Project map 
===========

![image](https://user-images.githubusercontent.com/9265326/33287171-de70bbf6-d3c8-11e7-8319-b4d69007fddb.png)

Developper links  
================

#### Code:
- [parsers](https://github.com/mini-kep/parsers)
- [database](https://github.com/mini-kep/db)
- [data browser](https://github.com/mini-kep/frontend-dash)  

#### Documentation:
- [Documentation](https://mini-kep.github.io/documentation)
- [API documentation](https://github.com/mini-kep/db/blob/master/README.md)

#### Workflow:
- [Trello issues](https://trello.com/b/ioHBMwH7/minikep) and [development notes](DEV.md) 
- [missing data map](https://github.com/mini-kep/datamap/blob/master/minikep_missing_values.ipynb) 
- [testing guidelines](https://github.com/mini-kep/guidelines/blob/master/testing.md)
