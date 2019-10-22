# cnblog.py
#
# Copyright @author chaoszh
# Time      2019/10/18
# Api docs  和风天气      https://dev.heweather.com/docs/api/weather
#           key         e5e387d4c0574dfe933bdebd5611797b

import requests as rq
import json

baseURL = "https://free-api.heweather.net/s6/weather/now?location=beijing&key=e5e387d4c0574dfe933bdebd5611797b"

def getWeather(position):
    url = "https://free-api.heweather.net/s6/weather/now?location="+position+"&key=e5e387d4c0574dfe933bdebd5611797b"
    data=rq.get(url)
    data=json.loads(data.text)['HeWeather6'][0]
    weather={
        'cond':data['now']['cond_txt'],
        'tmp':data['now']['tmp']
    }
    return weather