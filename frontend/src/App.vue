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
  <div class="flex flex-col lg:flex-row min-h-screen layout-wrapper"> 
    
    <SidebarComponent class="lg:w-64 w-full bg-blue-950 text-white shadow-2xl p-4" /> 
    
    <main class="flex-1 overflow-y-auto main-content-area">
      <HeaderComponent class="mb-8" /> 
      <RouterView /> 
    </main>
  </div>
</template>

<style scoped>
/* No se necesitan estilos con 'scoped' ya que todos los estilos ahora son globales o de Tailwind */
</style>

<style>
/* Estilos globales para la aplicación */
#app {
  /* Aseguramos que la app ocupe toda la altura */
  min-height: 100vh;
}

/* 1. Estilo para el contenedor general del Layout (donde está Sidebar y Main) */
.layout-wrapper {
  /* Usamos un fondo muy sutil y claro (igual que el QA estético) para que las tarjetas de las views destaquen */
  background: #f7f9fb; /* Un gris muy claro, casi blanco azulado */
}

/* 2. Estilo para el área principal de contenido (el <main> que envuelve RouterView) */
.main-content-area {
  padding: 2rem; /* Mantener un buen padding */
  flex-grow: 1;
  /* Asegurar que el contenido dentro pueda tener scroll si es necesario */
  overflow-y: auto;
}
</style>