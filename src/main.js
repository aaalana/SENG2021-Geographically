import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import Vuetify from  'vuetify'

import 'vuetify/dist/vuetify.min.css'
import VueRouter from 'vue-router'
import router from './router'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import sanitizeHTML from 'sanitize-html';

Vue.prototype.$sanitize = sanitizeHTML

Vue.use(VueRouter)

Vue.use(Vuetify, {
  icons: {
    iconfont: 'mdiSvg'
  }
})
Vue.config.productionTip = false

new Vue({
  router,
  // el: '#app', 
  render: h => h(App)
}).$mount('#app') // does almost the same thing as el: #app
