import Vue from 'vue'
import Router from 'vue-router'
import Homepage from '@/src/components/Homepage'
import Articlepage from '@/src/components/Articlepage'


Vue.use(Router)
export default new Router({
    mode: 'history',
    routes: [{
            path: '/',
            name: 'homepage',
            component: Homepage
        },
        {
            path: '/article',
            name: 'article',
            component: Articlepage,
        },
    ]
})