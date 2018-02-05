Introduction
============

```mini-kep``` is a collection of data parsers, database and a public end-user API that delivers macroeconomic time series. 
 Сurrent dataset includes Russian and some global macroeconomic data. 

The project goal is to provide open, machine-readable data for [reproducible](http://replication.uni-goettingen.de/wiki/index.php/Main_Page) macroeconomic research. It is inspired by
[St Louis FRED](https://fred.stlouisfed.org) and [Data Science Cookiecutter](https://drivendata.github.io/cookiecutter-data-science).


Project links
=============

The dataset is available through:
- [browser](http://macrodash.herokuapp.com)
- [listings](https://github.com/mini-kep/db/blob/master/doc/listing.md) *(TODO)*
- [pandas access code](https://github.com/mini-kep/user-charts/blob/master/access.py) 

Please see workflow map, developments notes and documentation [here](https://github.com/mini-kep/intro/blob/master/DEV.md).

[This repo](https://github.com/mini-kep/user-charts) has Jupiter notebooks and charts based on the dataset. 


Example
=======

Getting data from [a clean API](http://minikep-db.herokuapp.com/ru/series/GDP/a/yoy/1998/2017)
should be a lot better than going through [a MS Word file published by statistics agency.](http://www.gks.ru/wps/wcm/connect/rosstat_main/rosstat/ru/statistics/publications/catalog/doc_1140080765391)

Link:

- <http://minikep-db.herokuapp.com/ru/series/GDP/a/yoy/1998/2017>

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


Feedback
========

If you work with economic time series, please fill our [poll about data sources](https://goo.gl/2wY43R). 
Are you still relying on Excel or moving ahead?
