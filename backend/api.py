import json
import webapis.cnblog as cnblog
import webapis.cnodejs as cnodejs
import webapis.zhihudaily as zhihudaily
import webapis.heweather as heweather
import webapis.ip as ip

def getTopics():
    topics=[]
    # zhihudaily
    zhihudaily_topics=zhihudaily.getTopics()
    print("正在获取zhihu的文章*"+str(len(zhihudaily_topics)))
    for e in zhihudaily_topics:
        topics.append(e)
    # cnblogs
    cnblog_topics=cnblog.getTopics()
    print("正在获取cnblogs的文章*"+str(len(cnblog_topics)))
    for e in cnblog_topics:
        topics.append(e)
    cnodejs
    cnodejs_topics=cnodejs.getTopics()
    print("正在获取cnodejs的文章*"+str(len(cnodejs_topics)))
    for e in cnodejs_topics:
        topics.append(e)
    
    data = json.dumps(topics, ensure_ascii=False)
    return data


def getTopic(root, params):
    """
    params: id title author time
    """
    if root=='知乎':
        return json.dumps(zhihudaily.getTopic(params['id'],params['author']))
    elif root=='CNodejs':
        return json.dumps(cnodejs.getTopic(params['id']))
    elif root=='博客园':
        return json.dumps(cnblog.getTopic(params['id'],params['title'],params['author'],params['time']))

def getWeather(location):
    return json.dumps(heweather.getWeather(location))
    
def getLocation(_ip):
    return ip.getLocation(_ip)

def getIP():
    return ip.getIP()

if __name__ == "__main__":
    getTopics()