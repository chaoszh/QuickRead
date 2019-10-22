from flask import Flask, request, jsonify
from flask_cors import CORS
import api

app=Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.debug=True

@app.route('/')
def helloWorld():
    return 'Hello, World!'

@app.route('/api/topics')
def getTopics():
    return api.getTopics()

@app.route('/api/topic')
def getTopic():
    return api.getTopic(request.args['from'], request.args)

@app.route('/api/weather/<location>')
def getWeather(location):
    return api.getWeather(location)

@app.route('/api/city/<ip>')
def getLocation(ip):
    return api.getLocation(ip)

@app.route('/api/ip')
def getIP():
    return api.getIP()

# @app.route('/dailypic')
# def getPic():
#     import requests as rq
#     str = r"<img src='https://api.dujin.org/bing/1920.php' />"
#     return str

if __name__ == "__main__":
    CORS(app, supports_credentials=True)
    app.run()