import { createWebHistory, createRouter } from "vue-router";
import Home from '../views/HomeView.vue';
import comTest from '../components/ComTest.vue';
import login from '../components/loginFunc.vue'
import funcTest from "../components/funcTest.vue"

const routes = [
  {
    path: "/",
    component: Home,
  },
  {
    path: "/test",
    component: comTest,
  },
  {
    path: "/login",
    component: login,
  },
  {
    path: "/func",
    component: funcTest,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router; 