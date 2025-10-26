// En frontend/src/router/index.js

import { createRouter, createWebHistory } from 'vue-router';

// 1. Importaciones de VISTAS (Manteniendo el nombre 'Component' para Kiosco/Chatbot)
import KioscoComponent from '../views/KioscoComponent.vue'; // Mantienes el nombre Component
import ChatbotComponent from '../views/ChatbotComponent.vue'; // Mantienes el nombre Component
import HomeView from '../views/HomeView.vue';
import LoginView from '../views/LoginView.vue';
import RegisterView from '../views/RegisterView.vue'; 


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // RUTA PRINCIPAL (HOME)
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    // RUTAS DE AUTENTICACIÓN
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    },
    // RUTAS DEL SIMULADOR (Usando los nombres 'Component' originales)
    {
      path: '/kiosco',
      name: 'kiosco',
      component: KioscoComponent
    },
    {
      path: '/chatbot',
      name: 'chatbot',
      component: ChatbotComponent
    }
  ]
});

export default router;