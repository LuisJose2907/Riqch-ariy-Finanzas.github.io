<script setup>
// **IMPORTS NECESARIOS PARA EL TEMPLATE Y LA LÓGICA**
import { onMounted } from 'vue';
import axios from 'axios';
import HeaderComponent from '@/components/HeaderComponent.vue'; // Necesario para <HeaderComponent>
import SidebarComponent from '@/components/SidebarComponent.vue'; // Necesario para <SidebarComponent>
import { useSessionStore } from '@/stores/sessionStore'; // Necesario para la lógica de Pinia

// **INICIALIZACIÓN DE PINIA Y VARIABLES**
const sessionStore = useSessionStore();
const API_BASE_URL = import.meta.env.VITE_APP_API_URL; 

// **LÓGICA DE CARGA INICIAL (APIs 1 y 2)**
onMounted(async () => {
    if (!API_BASE_URL) {
        console.error("ERROR: VITE_APP_API_URL no está definida.");
        return;
    }
    
    try {
        // API 1: Obtener el Contexto 
        const contextResponse = await axios.get(`${API_BASE_URL}/geo/context`);
        sessionStore.setContexto(contextResponse.data); 

        // API 2: Obtener Productos
        const productsResponse = await axios.get(`${API_BASE_URL}/kiosco/productos`);
        sessionStore.setProductos(productsResponse.data);
        
    } catch (e) {
        console.error("Error crítico al cargar APIs 1/2. ¿El backend está corriendo?", e);
    }
});
</script>

<template>
  <div class="flex flex-col lg:flex-row min-h-screen bg-gray-50">
    <SidebarComponent class="lg:w-64 w-full bg-blue-900 text-white shadow-lg p-4" />
    <main class="flex-1 overflow-y-auto p-4 lg:p-8">
      <HeaderComponent class="mb-6 border-b pb-4" />
      <RouterView /> 
    </main>
  </div>
</template>

<style scoped>
/* Tu estilo aquí */
</style>