import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '../pages'
import LogIn from '../pages/login'
import Dashboard from '../pages/dashboard'
import Upload from '../pages/upload'
import Profile from '../pages/profile'
import Details from '../pages/coursedetails'
import Search from '../pages/search'
import Documents from '../pages/documents'
import MyCourses from '../pages/mycourses'
import CourseContents from '../pages/coursecontents'

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
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile
    },
    {
      path: '/coursedetails',
      name: 'Details',
      component: Details
    },
    {
      path: '/search',
      name: 'Search',
      component: Search
    },
    {
      path: '/documents',
      name: 'Documents',
      component: Documents
    },
    {
      path: '/mycourses',
      name: 'MyCourses',
      component: MyCourses
    },
    {
      path: '/coursecontents',
      name: 'CourseContents',
      component: CourseContents
    }
  ]
})
