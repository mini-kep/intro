Goal
====

Provide open, machine-readable data for [reproducible](http://replication.uni-goettingen.de/wiki/index.php/Main_Page) macroeconomic research.


#### Motivational example

Using data from [this API call](http://minikep-db.herokuapp.com/ru/series/GDP/a/yoy/1998/2017)
should be quicker and cleaner than going through [a MS Word file published by a statistics agency.](http://www.gks.ru/wps/wcm/connect/rosstat_main/rosstat/ru/statistics/publications/catalog/doc_1140080765391)

<table border=0>
<tr><td align=center>:page_with_curl: :chart_with_upwards_trend: :wink:</td>
       <td align=center>:mountain_bicyclist: :tired_face: :question: </td>
</tr>

<tr>
<td valign=top>
<img src="https://user-images.githubusercontent.com/9265326/34766088-61c4fc8a-f604-11e7-8bc4-1682121fbf88.png">
</td>

<td valign=top>
<img src="https://user-images.githubusercontent.com/9265326/34765386-6790f30a-f602-11e7-90dc-5a5ca5c0bffd.png">

</td>
</tr></table>


Introduction
============

```mini-kep``` is a collection of data parsers, database and a public end-user API 
that delivers macroeconomic time series.

The current dataset includes Russian and some global macroeconomic data. It is available through:
- [data browser](http://macrodash.herokuapp.com)
- [variable listing](https://github.com/mini-kep/db/blob/master/doc/listing.md)
- [pandas access code](https://github.com/mini-kep/user-charts/blob/master/access.py) 

[This repo](https://github.com/mini-kep/user-charts) has notebooks and charts based on the dataset. 

Inspiration  
===========

Project influenced by:
- [St Louis FRED](https://fred.stlouisfed.org) 
- [Data Science Cookiecutter](https://drivendata.github.io/cookiecutter-data-science)


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

Project map 
===========

![image](https://user-images.githubusercontent.com/9265326/33287171-de70bbf6-d3c8-11e7-8319-b4d69007fddb.png)


Feedback
========

If you work with economic time series, please fill our [poll about data sources](https://goo.gl/2wY43R)
to help us understand user needs.

