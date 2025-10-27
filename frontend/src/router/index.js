// En frontend/src/router/index.js

import { createRouter, createWebHistory } from 'vue-router';

// 1. Importaciones de VISTAS
import KioscoComponent from "../components/KioscoComponent.vue";
import ChatbotComponent from '../components/ChatbotComponent.vue';
import HomeView from '../views/HomeView.vue';
import LoginView from '../views/LoginView.vue';
import RegisterView from '../views/RegisterView.vue';
import ProfessorDashboard from '../views/ProfessorDashboard.vue'; // <-- ¡NUEVA IMPORTACIÓN!


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
    // RUTAS DEL SIMULADOR
    {
      path: '/kiosco',
      name: 'kiosco',
      component: KioscoComponent
    },
    {
      path: '/chatbot',
      name: 'chatbot',
      component: ChatbotComponent
    },
    // RUTA DEL MODELO MARS / DASHBOARD DEL PROFESOR
    {
        path: '/profesor/dashboard',
        name: 'ProfessorDashboard',
        component: ProfessorDashboard // <-- ¡NUEVA RUTA!
    }
  ]
});

export default router;