<template>
  <div class="kiosco-view">
    <h2 class="text-3xl font-extrabold text-gray-900 mb-8">
      Mercado Local: Catálogo de Productos
    </h2>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <ProductCard 
        v-for="product in products" 
        :key="product.id" 
        :product="product"
        @comprar="handleCompra"
      />
    </div>

    <p v-if="products.length === 0" class="text-gray-500 mt-10">Cargando productos o P2 no está corriendo...</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import ProductCard from '@/components/ProductCard.vue'

const API_BASE_URL = import.meta.env.VITE_APP_API_URL 

const products = ref([])
const region = 'Lima' // Se usará la data de App.vue más adelante

const fetchProducts = async () => {
  if (!API_BASE_URL) return
  try {
    // Llama a API 2: /kiosco/products/{region}
    const response = await axios.get(`${API_BASE_URL}/kiosco/products/${region}`)
    products.value = response.data
  } catch (error) {
    console.error("Error al cargar productos (API 2).", error)
  }
}

const handleCompra = (productId) => {
    // PENDIENTE: Aquí se implementará la API 3 (Transacciones) en el Bloque 8–12h.
    console.log(`Solicitud de compra para ID: ${productId}. Pendiente de implementar API 3.`)
}

onMounted(fetchProducts)
</script>