#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 17/Sep/2015
# File: multiprocessingrobust.py
# Desc: use multiprocessing test the robustness of crawler-slave with
#   douban book api
#
# Produced By BR(BeautifulReading)
import multiprocessing
from util import loadIsbns
from itertools import cycle
import json
from Download import Download

def worker(appids, isbns):
    appidsCycle = cycle(appids)

    for isbn in isbns:
        url = 'http://' + appidsCycle.next() + '.appspot.com/url?url=' + 'http://book.douban.com/isbn/' + isbn
        print 'DEBUG: ', url

        d = Download(url)
        if d.doRequest():
            print isbn, 'network error'
            continue

        j = json.loads(d.getSOURCE())
        print isbn, j['status_code']

    return

if __name__ == '__main__':
    isbns = loadIsbns('isbns.txt')
    appids = loadIsbns('appids')

    jobs = []
    for i in range(10):
        p = multiprocessing.Process(target=worker,args = (appids[(800 * i):(i * 800 + 800)], isbns))
        jobs.append(p)
        p.start()
