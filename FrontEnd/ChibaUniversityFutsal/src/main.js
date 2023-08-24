import './assets/main.css'

import { createApp, ref } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store';
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'
import vuetify from "./plugins/vuetify";

const app = createApp(App);

app.use(router);
app.use(vuetify);
const childId = ref('');
app.provide(/* key */ 'childId', /* value */ childId);

app.mount('#app');
