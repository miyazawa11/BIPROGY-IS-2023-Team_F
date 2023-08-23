import { createRouter, createWebHistory } from 'vue-router'
import SelectView from '../views/SelectView.vue';
import AttendanceView from '../views/AttendanceView.vue';
import SendConfirmView from '../views/SendConfirmView.vue';
import KidsListView from '../views/KidsListView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'selectPage',
      component: SelectView
    },
    {
      path: '/guardians/attend',
      name: 'attendPage',
      component: AttendanceView
    },
    {
      path: '/guardians/confirm',
      name: 'SendConfirmPage',
      component: SendConfirmView
    },
    {
      path: '/nursery/confirm',
      name: 'KidsListViewPage',
      component: KidsListView
    }
  ]
})

export default router
