import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Text2Speech from './views/Text2Speech.vue'
import Image2Text from './views/Image2Text.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/text2speech',
      name: 'text2speech',
      component: Text2Speech
    },
    {
      path: '/image2Text',
      name: 'image2Text',
      component: Image2Text
    },
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    }
  ]
})
