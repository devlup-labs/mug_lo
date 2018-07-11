import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '../pages'
import LogIn from '../pages/login'
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '/login',
      name: 'LogIn',
      component: LogIn
    }
  ]
})
