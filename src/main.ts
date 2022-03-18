import { createApp } from 'vue'
import App from './App.vue'
import store from './common/store'
import router from './router/router'

createApp(App).use(store).use(router).mount('#app')
