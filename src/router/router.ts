import { createWebHistory, createRouter } from "vue-router";
import Space from '../assets/space';



const routes = [
  {
    path: "/space",
    component: Space,
  },

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router; 