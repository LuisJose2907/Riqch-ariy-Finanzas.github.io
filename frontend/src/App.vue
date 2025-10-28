<script setup>
// **IMPORTS NECESARIOS PARA EL TEMPLATE Y LA LÓGICA**
import { ref, onMounted } from 'vue'; 
import axios from 'axios';
import HeaderComponent from '@/components/HeaderComponent.vue'; 
import SidebarComponent from '@/components/SidebarComponent.vue'; 
import RetoDelSolModal from '@/components/RetoDelSolModal.vue'; 
import { useSessionStore } from './stores/session.js';

// **INICIALIZACIÓN DE PINIA Y VARIABLES**
const sessionStore = useSessionStore();
const API_BASE_URL = import.meta.env.VITE_APP_API_URL; 

// Estado para forzar la recarga de componentes después de un evento (API 6)
const lastUpdatedKey = ref(Date.now()); 

// **LÓGICA DE CARGA INICIAL (APIs 1 y 2)**
const fetchInitialData = async () => {
    if (!API_BASE_URL) {
        console.error("ERROR: VITE_APP_API_URL no está definida.");
        return;
    }
    
    try {
        // API 1: Obtener el Contexto 
        //const contextResponse = await axios.get(`${API_BASE_URL}/geo/context`);
        //sessionStore.setContexto(contextResponse.data); 

        // Las llamadas reales al backend están comentadas
        console.warn("********************************************************");
        console.warn("MODO DE DESARROLLO: ¡El backend está desconectado!");
        console.warn("Usando datos 'mock' (falsos) para el frontend.");
        console.warn("********************************************************");


        // --- MOCK API 1: Obtener el Contexto ---

  
        // Datos falsos para el contexto:
        const fakeContext = {
          id: "user_123",
          nombre: "Usuario de Prueba",
          region: "lima",
          configuraciones: { tema: "oscuro" }
        };
        sessionStore.setContexto(fakeContext); // Usamos el objeto falso

        // API 2: Obtener Productos
        //const productsResponse = await axios.get(`${API_BASE_URL}/kiosco/productos`);
        //sessionStore.setProductos(productsResponse.data);
        //
        //// Cargar estadísticas del usuario al inicio (API 5)
        //sessionStore.fetchUserStats(); 

        const fakeProducts = [
          { id: "prod_A", nombre: "Chizito Falso", precio: 1.50, stock: 10 },
          { id: "prod_B", nombre: "Inka Kola Falsa", precio: 2.50, stock: 5 },
  ];
  sessionStore.setProductos(fakeProducts); // Usamos el array falso

        
    } catch (e) {
        console.error("Error crítico al cargar APIs iniciales. ¿El backend está corriendo?", e);
    }
}

onMounted(fetchInitialData);

// FUNCIÓN CLAVE PARA RECARGAR TODO EL ESTADO DESPUÉS DEL EVENTO DEL PROFESOR
const recargarTodo = async () => {
    console.log("Evento 'Reto del Sol' aplicado. Recargando datos...");
    
    // 1. Vuelve a llamar a la API 2 (Productos) - Actualiza Kiosco
    await fetchInitialData(); 
    
    // 2. 🎯 CRUCIAL: Recarga los datos del Sidebar (Saldo/Inventario - API 5)
    // Asumiendo que esta acción YA EXISTE en tu Pinia Store.
    sessionStore.fetchUserStats(); 
    
    // 3. Forzar el re-render de las Vistas (RouterView y KioscoComponent)
    lastUpdatedKey.value = Date.now(); 
};
</script>

<template>
  <div class="flex flex-col lg:flex-row min-h-screen layout-wrapper"> 
    
    <SidebarComponent class="lg:w-64 w-full bg-blue-950 text-white shadow-2xl p-4" /> 
    
    <main class="flex-1 overflow-y-auto main-content-area">
      <HeaderComponent class="mb-8" /> 

      <div class="mb-8 flex justify-end">
        <RetoDelSolModal 
          :region="sessionStore.contextoRegional.region"
          @reto-aplicado="recargarTodo" 
        />
      </div>
      
      <RouterView :key="lastUpdatedKey" /> 
      
    </main>
  </div>
</template>

<style scoped>
/* No se necesitan estilos con 'scoped' ya que todos los estilos ahora son globales o de Tailwind */
</style>

<style>
/* Estilos globales para la aplicación */
#app {
  min-height: 100vh;
}

.layout-wrapper {
  background: #f7f9fb; 
}

.main-content-area {
  padding: 2rem; 
  flex-grow: 1;
  overflow-y: auto;
}
</style>