import Vue from 'vue'
import App from './App.vue'
import router from './router'


//引入js
// import $ from 'jQuery'
import api from './js/api.js'

//引入css
import '@/src/css/bootstrap.css'
import '@/src/css/jumbotron.css'
import '@/src/css/common.css'

// Vue.prototype.$ = $;
Vue.prototype.api = api;
Vue.config.productionTip = false;

// console.log(router)

new Vue({
    router: router,
    render: h => h(App),
}).$mount('#app')