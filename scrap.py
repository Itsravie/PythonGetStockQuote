## import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import time

## define page to hit
quote_page = 'https://www.lseg.com/'

## function declaration to do job
def readSomeUrl(page):
    soup = BeautifulSoup(page, 'html.parser')
    divElement = soup.find('div', attrs={'class': 'currency-price'})
    data = divElement.text.strip()
    tagData = data.split('\n')

    index = divElement.find('p', attrs = {'class' : 'header-currency-number'})
    indexHeader = divElement.find('p', attrs = {'class' : 'header-shareprice-text'})
    currency = divElement.find('p', attrs = {'class' : 'header-shareprice-currency'})

    timeNow = datetime.now().time().strftime('%H:%M:%S') + ' >> '
    print(timeNow, indexHeader.text, 'for the london stock exchange index is ', index.text, ' [' , currency.text , ']')

    ## write results to csv
    with open('lse_index.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(['lse index', indexHeader.text, index.text, currency.text])

## define interval and iterations
everyXSeconds = 30.0
iterations = 50

## call function in loop
urlToHit = quote_page
for iter in range(1,iterations):
    time.sleep(everyXSeconds)
    readSomeUrl(urlopen(urlToHit))

print('The End. Thanks. Data has been writter to lse_index.csv')
## the end
