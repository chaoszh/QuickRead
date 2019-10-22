# cnblog.py
#
# Copyright @author chaoszh
# Time      2019/10/18
# Api       http://ip.taobao.com/service/getIpInfo.php

import requests as rq
import re
import json

def getLocation(ip):
    url="http://ip.taobao.com/service/getIpInfo.php?ip="+ip
    res=rq.get(url,'get')
    city=json.loads(res.text)['data']['city']
    return city

def getIP():
    res=rq.get("https://pv.sohu.com/cityjson?ie=utf-8",'get')
    res=re.search('{(.*)?}',res.text).group()
    ip=json.loads(res)['cip']
    return ip