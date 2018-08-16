import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '../pages'
import LogIn from '../pages/login'
import Dashboard from '../pages/dashboard'
import Upload from '../pages/upload'

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
    },
    {
      path: '/password-reset',
      name: 'password-reset',
      component: LogIn
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: '/upload',
      name: 'Upload',
      component: Upload
    }
  ]
})
