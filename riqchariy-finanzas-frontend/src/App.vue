<script setup></script>

<template>
  <div class="flex flex-col lg:flex-row min-h-screen bg-gray-50">

    <SidebarComponent class="lg:w-64 w-full bg-blue-900 text-white shadow-lg p-4" />

    <main class="flex-1 overflow-y-auto p-4 lg:p-8">

      <HeaderComponent class="mb-6 border-b pb-4" />

      <RouterView /> 

    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue' 
import axios from 'axios'
import { RouterView } from 'vue-router'
import HeaderComponent from '@/components/HeaderComponent.vue' 
import SidebarComponent from '@/components/SidebarComponent.vue' 

// 1. LECTURA CRÍTICA: Obtener la URL de la variable de entorno (.env o Azure)
const API_BASE_URL = import.meta.env.VITE_APP_API_URL

const contextoRegional = ref(null) 

onMounted(async () => {
  // 2. Control de error si la variable no está definida
  if (!API_BASE_URL) {
    console.error("VITE_APP_API_URL no está definida. Verifique su archivo .env o la configuración de Azure.")
    return
  }

  try {
    // 3. Uso de la URL para la llamada a API 1: /geo/context
    const response = await axios.get(`${API_BASE_URL}/geo/context`) 

    contextoRegional.value = response.data 

    console.log("Contexto de la Sesión:", contextoRegional.value)

  } catch (error) {
    console.error("Error de Integración Temprana con API 1. Verifique que P2 esté ejecutándose:", error)
  }
})
</script>

<style scoped></style>
