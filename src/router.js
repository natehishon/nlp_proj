import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from './components/HelloWorld'
import Api from './views/Api.vue'
import { BootstrapVue, IconsPlugin, ModalPlugin } from 'bootstrap-vue'

Vue.use(Router)
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(ModalPlugin)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: HelloWorld
    },
    {
      path: '/api',
      name: 'api',
      component: Api
    }
  ]
})
