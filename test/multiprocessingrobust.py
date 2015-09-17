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

def worker(appid, isbn):
    print 'Worker'
    return

if __name__ == '__main__':
    jobs = []
    for i in range(10):
        p = multiprocessing.Process(target=worker,args = (appid, isbn))
        jobs.append(p)
        p.start()
