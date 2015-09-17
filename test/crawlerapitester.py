#!/usr/bin/env python
#
# Usage: python crawlerapitester.py 10
#
from Download import Download
import json
import sys

url = 'http://csrgxtu01.appspot.com/url?url=http://book.douban.com/isbn/9787508653594'

for i in range(int(sys.argv[1])):
    d = Download(url)
    if d.doRequest():
        print i, 'cant doRequest'
        continue

    j = json.loads(d.getSOURCE())
    print i, j['err'], j['status_code']
