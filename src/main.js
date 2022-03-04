import { createApp } from 'vue'
import App from './App.vue'
import store from './common/store.js'

createApp(App).use(store).mount('#app')
