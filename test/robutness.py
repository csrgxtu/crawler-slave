#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 17/Sep/2015
# File: robutness.py
# Desc: test the robutness of the crawler-slave with douban book url
#
# Produced By BR(BeautifulReading)
from Download import Download
from util import loadIsbns
import json

baseUrl = 'http://book.douban.com/isbn/'
isbns = loadIsbns('isbns.txt')

count = 0
for isbn in isbns:
    url = baseUrl + isbn
    d = Download(url)
    if d.doRequest():
        print isbn, 'network error'
        continue

    j = json.loads(d.getSOURCE())
    if j['status_code'] eq 200:
        count = count + 1

    print isbn, j['status_code']

print 'Status: ', count, len(isbns)
