# cnblog.py
#
# Copyright @author chaoszh
# Time      2019/10/18
# Api docs  http://wcf.open.cnblogs.com/blog/help

import requests as rq
import json
from bs4 import BeautifulSoup as bs
import html
import re
from webapis.common import cssFilter

baseURL = "http://wcf.open.cnblogs.com/blog"

headers = {
    'Accept':'*/*',
#     'Accept-Encoding':'gzip, deflate, br',            这个只有浏览器能设置，是属于浏览器的解压工作
    'accept-language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
#     'Content-Length':'151',
    'content-type':'application/xml',
#     'Cookie':cookie,
#     'Host':host,
#     'Origin':origin,
#     'Referer':referer,
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
#     'x-csrf-token':token
}

def get(url):
    return rq.get(baseURL+url, headers=headers)

data = get('/TenDaysTopDiggPosts/10')
soup = bs(data.text,'lxml')
entry_list=soup.find_all('entry')
entry_list

# /topics
def getTopics():
    data = get('/TenDaysTopDiggPosts/10')
    soup = bs(data.text,'lxml')
    entry_list=soup.find_all('entry')
    articles=[]
    for i in entry_list:
        article={
            'id':i.id.get_text(),
            'title':i.title.get_text(),
            'author':i.author.find('name').get_text(),
            'time':i.published.get_text(),
            'content':i.summary.get_text(),
            'from':'博客园',
        }
        articles.append(article)
    return articles

# /topic
def getTopic(id, title, author, time):
    data = get('/post/body/'+str(id))
    content = bs(data.text,'lxml').find('string').get_text()
    content = html.unescape(content)
    content = cssFilter(content)
    with open('topics.html','w',encoding='utf-8') as f:
        f.write(content) 
    topic={
        'title':title,
        'author':author,
        'time':time,
        'content':content
    }
    return topic