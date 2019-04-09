import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Ping from '@/components/Ping';

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/contactUs',
      name: 'contactUs',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/ContactUs.vue')
    },
    {
      path: '/map',
      name: 'map',
      component: () => import('./views/Maps.vue')
    },
    {
      path: '/blog',
      name: 'blog',
      component: () => import('./views/Blog.vue')
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: () => import('./views/Dashboard.vue')
    },
    {
      path: '/tripPlanning',
      name: 'tripPlanning',
      component: () => import('./views/TripPlanning.vue')
    },
    {
      path: '/myProfile',
      name: 'myProfile',
      component: () => import('./views/MyProfile.vue')
    },
    //test route for backend
    {
      path: '/Ping',
      name: 'Ping',
      component: Ping,
    },
    // 404 page not found 
    {
      path: '*',
      name: 'NotFound',
      component: () => import('./views/NotFound.vue')
    }
  ]
})
