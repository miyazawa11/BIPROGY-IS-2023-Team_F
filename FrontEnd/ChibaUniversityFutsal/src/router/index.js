import { createRouter, createWebHistory } from 'vue-router'
import SelectView from '../views/SelectView.vue';
import AttendanceView from '../views/AttendanceView.vue';
import SendConfirmView from '../views/SendConfirmView.vue';
import KidsListView from '../views/KidsListView.vue'
import KidDetailView from '../views/KidDetailView.vue'
import AttentionView from '../views/AttentionView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'selectPage',
      component: SelectView
    },
    {
      path: '/guardians/:id',
      name: 'attendPage',
      component: AttendanceView
    },
    {
      path: '/guardians/confirm/:id',
      name: 'SendConfirmPage',
      component: SendConfirmView
    },
    {
      path: '/guardians',
      name: 'AttentionViewPage',
      component: AttentionView
    },
    {
      path: '/nursery/confirm',
      name: 'KidsListViewPage',
      component: KidsListView
    },
    {
      path: '/nursery/confirm/detail/:id',
      name: 'KidDetailViewPage',
      component: KidDetailView
    }
  ]
})

export default router
