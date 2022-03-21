import { createWebHistory, createRouter } from "vue-router";
import Space from '../assets/space';
import comTest from '../components/ComTest.vue';


const routes = [
  {
    path: "/space",
    component: Space,
  },
  {
    path: "/test",
    component: comTest,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router; 