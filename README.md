# Wuhan Coronavirus Data Collection

## About

This repo is for sharing the data collected using a python crawler on dxy.com.

The data is collected each day at about 12 pm(noon).

The csv file starts with the exact collection time and an overview of the whole country. It includes fields: **Province**, **Confirmed**, **Suspected**, **Cured**, and **Death**.

The names of provinces and cities are in Chinese, ordered by the number of *confirmed cases*.

The data is formatted in csv and can be easily used by MATLAB, Excel, or other programs.

For some reason, the suspected cases are not displayed for each city and province on dxy.com. Therefore, the suspected count is always 0, which means it is meaningless. 

## Processing

I used the the crawler and data for my own modeling with Python and MATLAB. I also used other python program to process the data in order to use them in different analysis. 

For example, I've compiled the data to show the changes for each province and output a file for each province. They contain data in a timeline for that province and can be used to generate graphs in MATLAB. 

All other data processing programs are in [this](https://github.com/EthanGeekFan/wuhan-coronavirus-data/tree/master/Processors) Processors directory.

## The Crawler

The crawler, writen in Python 3, is published on [PyPI as a package](https://pypi.org/project/nCoV/) and its source is in [this](https://github.com/EthanGeekFan/nCoV) repository.
