import { createRouter, createWebHistory } from 'vue-router'
import SelectView from '../views/SelectView.vue';
import AttendanceView from '../views/AttendanceView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'selectPage',
      component: SelectView
    },
    
    {
      path: '/attend',
      name: 'attendPage',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: AttendanceView
    }
    
  ]
})

export default router
