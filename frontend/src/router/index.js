import { createRouter, createWebHistory } from 'vue-router'
import IndexView from '../views/IndexView.vue'
import ItemView from '../views/ItemView.vue'
import LoginView from '../views/LoginView.vue'
import SignUpView from '../views/SignUpView.vue'
import LogoutView from '../views/LogoutView.vue';
import ProfileView from '../views/ProfileView.vue';


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'index',
      component: IndexView,
    },
    {
      path: '/item/:id',
      name: 'item',
      component: ItemView,
    },
    {
      path: '/signup/',
      name: 'signup',
      component: SignUpView,
    },
    {
      path: '/login/',
      name: 'login',
      component: LoginView,
      props: true,
    },
    {
      path: '/logout/',
      name: 'logout',
      component: LogoutView,
    },
    {
      path: '/profile/',
      name: 'profile',
      component: ProfileView,
    }
  ]
})

export default router
