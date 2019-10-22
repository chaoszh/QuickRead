/* httpRequest.js
 * Copyright @author: chaoszh
 * Time 2019-10-17
 */

/*axios*/
//httpRequest
import axios from 'axios'
import qs from 'qs'

var baseURL = 'http://localhost:5000';

axios.defaults.baseURL = baseURL; //配置接口地址

function httpRequest(url, method, params = {}) {
    return new Promise((resolve, reject) => {
        console.log('[CHAOSZH]', method.toUpperCase(), baseURL + url + qs.stringify(params));
        axios({
            method: method,
            url: url,
            params: params,
            withCredentials: false,
        }).then(res => {
            resolve(res);
        }).catch(err => {
            reject(err);
        })
    })
}

export default {
    httpRequest,
}