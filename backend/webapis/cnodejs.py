# cnodejs.py
#
# Copyright @author chaoszh
# Time      2019/10/18
# Api docs  https://cnodejs.org/api/

import requests as rq
import json
import re

from webapis.common import cssFilter


baseURL = "https://cnodejs.org/api/v1"

def get(url):
    return rq.get(baseURL+url)

# /topics
def getTopics():
    data = get('/topics').text
    res = json.loads(data)['data']

    articles=[]
    for i in range(len(res)):
        if res[i]['visit_count']<80000:
            continue
        content = re.sub(r'\n','',res[i]['content'])
        # with open('topics.html','w',encoding='utf-8') as f:
            # f.write(content) 
        article={
            'id':res[i]['id'],
            'title':res[i]['title'],
            'author':res[i]['author']['loginname'],
            'content':content,
            'from':'CNodejs'
        }
        articles.append(article)
        return articles

# topic
def getTopic(id):
    data = get('/topic/'+id).text
    res = json.loads(data)['data']
    content = re.sub(r'\n','',res['content'])
    content = cssFilter(content)
    article={
        'title':res['title'],
        'author':res['author']['loginname'],
        'time':res['create_at'],
        'content':content
    }
    return article