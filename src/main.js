import { createApp } from 'vue'
import App from './App.vue'
import store from './common/store.js'
import router from './common/router'

createApp(App).use(store).use(router).mount('#app')
