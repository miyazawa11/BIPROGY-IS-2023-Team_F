import { createRouter, createWebHistory } from 'vue-router'
import SelectView from '../views/SelectView.vue';
import AttendanceView from '../views/AttendanceView.vue';
import SendConfirmView from '../views/SendConfirmView.vue'

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
      component: AttendanceView
    },
    {
      path: '/confirm',
      name: 'SendConfirmPage',
      component: SendConfirmView
    }
  ]
})

export default router
