import httpRequest from './httpRequest'
var htr = httpRequest.httpRequest;
import $ from 'jquery'

//example
var example = function() {
    //htr返回一个Promise
    return htr('https://api.github.com/users/ChaosZh', 'get', {});
    //前端得到数据的办法：
    // async function getData(){
    //     return await example();
    // }
}

var getWeather = function(location) {
    let url = '/api/weather/' + location;
    return htr(url, 'get', {});
}

var getTopics = function() {
    let url = '/api/topics';
    return htr(url, 'get', {});
}

var getTopic = function(params) {
    let url = '/api/topic'
    return htr(url, 'get', params);
}

var getLocation = function(ip) {
    let url = 'api/city/' + ip;
    return htr(url, 'get', {});
}

var getIP = function() {
    // new Promise((resolve, reject) => {
    //     $.ajax({
    //         url: 'https://pv.sohu.com/cityjson?ie=utf-8?callback=?', //不指定回调名，可省略callback参数，会由jQuery自动生成
    //         dataType: 'jsonp',
    //         jsonpCallback: 'demo',
    //         headers:{
    //             'Cookie':'SUV=1906201810247773; reqtype=pc; gidinf=x099980109ee0fef7b5ef04780009d3740c337cf1cf4; _muid_=1566997018861142; MTV_SRC=11100001; t=1571240396746; IPLOC=CN3101; SameSite=None; Secure='
    //         },
    //         // crossDomain: true,
    //         success: function(data) {
    //           console.log(data.msg);
    //         }
    //     });
    // })
    let url = ('api/ip');
    return htr(url,'get',{});
}

export default {
    example,
    htr,
    getWeather,
    getTopics,
    getTopic,
    getLocation,
    getIP
}