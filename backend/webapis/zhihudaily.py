# zhihudaily.py
#
# Copyright @author chaoszh
# Time      2019/10/18
# Api docs  ----------------
#           知乎专栏
#           https://github.com/TonnyL/Zhihu_Zhuanlan_APIs/wiki
#           知乎日报
#           https://github.com/izzyleung/ZhihuDailyPurify/wiki/%E7%9F%A5%E4%B9%8E%E6%97%A5%E6%8A%A5-API-%E5%88%86%E6%9E%90

import requests as rq
import re
import json
from bs4 import BeautifulSoup as bs
from webapis.common import cssFilter

baseURL = "https://news-at.zhihu.com/api/4"

headers = {
    'Accept':'*/*',
    'accept-language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'content-type':'application/json',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
}

def get(url):
    return rq.get(baseURL+url, headers=headers)

# /topics
def getTopics():
    data = get('/news/latest').text
    res = json.loads(data)
    stories = res['stories']
    topics=[]
    for s in stories:
        topic = {
            'id':s['id'],
            'title':s['title'],
            'author':s['hint'],
            'from': '知乎',
        }
        content = get('/news/'+str(topic['id'])).text
        content = json.loads(content)
        content = re.sub(r'\r\n','',content['body'])
        content = re.sub(r'\n','',content)
        content = bs(content).find('div',{'class':'content'}).get_text()
        content = cssFilter(content)
        # print(content)
        topic['content']=content
        topics.append(topic)
    return topics

# topic
def getTopic(id, author):
    data = get('/news/'+str(id)).text
    res = json.loads(data)
    content = re.sub(r'\r\n','',res['body'])
    content = re.sub(r'\n','',content)

    content = str(bs(content).find('div',{'class':'content'}))
    # with open('topics.json','w',encoding='utf-8') as f:
    #     f.write(content) 
    topic = {
        'title': res['title'],
        'author': author,
        'content': content,
    }
    return topic