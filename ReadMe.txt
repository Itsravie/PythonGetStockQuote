PythonGetStockQuote is meant to work on Python 3.
Specific version used for this application is Python 3.6.5
To check your python version, type python --version in your terminal.
We have used VSCode as editor for python.

First block:
## import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import time

Libraries used are
a) urllib.request => a Python module for fetching URLs (Uniform Resource Locators). It offers a very simple interface, in the form of the urlopen function.
b) Beautiful Soup => a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping.
version used for this application is  4.6.0
c) datetime module => supplies classes for manipulating dates and times in both simple and complex ways
d) csv module => handy approach to read, write, append csv files in python
e) time module => we have used method sleep() to suspend execution for the given number of seconds

## define page to hit
quote_page = 'web page you are targeting'   
to reiterate - this application is just for learning purpose. do no spam this or any webpage by running indefinately. Respect your resource and respect other's resource.

## function declaration to do job
def readSomeUrl(page)
    ...
actual action happends here. from soup reading url to tag parsing to print our target to csv append.

## call action method iteratively, in given intervals

##Thank you for reading.
