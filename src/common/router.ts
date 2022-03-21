import { createWebHistory, createRouter } from "vue-router";
import Space from '../assets/space';
import comTest from '../components/ComTest.vue';
import login from '../components/loginFunc.vue'

const routes = [
  {
    path: "/space",
    component: Space,
  },
  {
    path: "/test",
    component: comTest,
  },
  {
    path: "/login",
    component: login,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router; 