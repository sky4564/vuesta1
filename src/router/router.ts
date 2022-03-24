import { createWebHistory, createRouter } from "vue-router";
import Space from '../assets/space';
import TestView from '../views/TestView.vue';
import HomeView from '../views/HomeView.vue';



const routes = [
  {
    path: "/",
    component: HomeView,
  },
  {
    path: "/space",
    component: Space,
  },
  {
    path: "/test",
    component: TestView,
  },

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router; 