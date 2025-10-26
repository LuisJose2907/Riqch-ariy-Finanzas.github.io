<script setup>
import { useSessionStore } from '@/stores/sessionStore';
import { computed } from 'vue';
// Asegúrate de que la ruta a tu ProductCard es correcta
import ProductCard from '@/components/ProductCard.vue'; 

const sessionStore = useSessionStore();

// 1. OBTENER PRODUCTOS DE PINIA (API 2)
// Usamos el getter de Pinia que ya tiene la lista de productos cargada por App.vue
const productos = computed(() => sessionStore.productosDisponibles);

// 2. FUNCIÓN PARA MANEJAR LA COMPRA (LLAMA A LA API 3)
const handleCompra = async (productId) => {
    // Llama a la acción de Pinia: realiza la llamada POST a la API 3, 
    // y luego ACTUALIZA el saldo y el inventario en el store.
    await sessionStore.realizarTransaccion(productId);
    
    // El sidebar (SidebarComponent.vue) se actualizará automáticamente aquí.
};
</script>

<template>
    <div class="kiosco-view">
        <h1 class="text-3xl font-semibold mb-6 text-gray-800">
            🛒 Mi Kiosco Escolar
        </h1>
        
        <div v-if="productos.length === 0" class="text-center p-10 text-gray-500">
            Cargando productos o la API 2 no está disponible.
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <ProductCard 
                v-for="product in productos"
                :key="product.id"
                :product="product"
                @buy="handleCompra(product.id)" 
            />
        </div>
    </div>
</template>

<style scoped>
/* Estilos si son necesarios */
</style>