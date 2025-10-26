// src/router/index.js

import { createRouter, createWebHistory } from 'vue-router'
// Importar los componentes de las vistas
import KioscoComponent from '@/components/KioscoComponent.vue'
import ChatbotComponent from '@/components/ChatbotComponent.vue' 

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      // RUTA PRINCIPAL: El Kiosco es la vista por defecto
      path: '/',
      name: 'kiosco',
      component: KioscoComponent 
    },
    {
      // RUTA SECUNDARIA: El Chatbot se carga aquí
      path: '/chatbot',
      name: 'chatbot',
      component: ChatbotComponent 
    }
  ]
})

export default router