import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import {
  Vuetify,
  VApp,
  VCard,
  VCheckbox,
  VNavigationDrawer,
  VFooter,
  VList,
  VBtn,
  VIcon,
  VGrid,
  VTabs,
  VDivider,
  VToolbar,
  VTextField,
  VParallax,
  transitions
} from 'vuetify'
import '../node_modules/vuetify/src/stylus/app.styl'
import 'font-awesome/css/font-awesome.css'
import httpClient from './plugins/httpClient'

Vue.use(httpClient)

Vue.use(Vuetify, {
  components: {
    VApp,
    VCard,
    VCheckbox,
    VNavigationDrawer,
    VFooter,
    VList,
    VBtn,
    VIcon,
    VGrid,
    VTabs,
    VDivider,
    VToolbar,
    VTextField,
    VParallax,
    transitions
  },
  theme: {
    primary: 'blue',
    secondary: '#424242',
    accent: '#82B1FF',
    error: '#FF5252',
    info: '#2196F3',
    success: '#4CAF50',
    btncolor: '#2196f3',
    warning: '#FFC107'
  }
})

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
