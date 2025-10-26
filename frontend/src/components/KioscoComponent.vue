<script setup>
import { useSessionStore } from '@/stores/sessionStore';
import { computed } from 'vue';
// Asegúrate de que la ruta a tu ProductCard es correcta
import ProductCard from '@/components/ProductCard.vue'; 

const sessionStore = useSessionStore();

// 1. OBTENER PRODUCTOS DE PINIA (API 2)
const productos = computed(() => sessionStore.productosDisponibles);

// 2. FUNCIÓN PARA MANEJAR LA COMPRA (LLAMA A LA API 3)
const handleCompra = async (productId) => {
    // Añade el bloque try...catch para manejar visualmente los errores
    try {
        console.log(`Iniciando compra para Producto ID: ${productId}`);
        
        // Llama a la acción de Pinia. La acción manejará la lógica de la API 3
        // y actualizará el store.
        await sessionStore.realizarTransaccion(productId);
        
        // LÍNEA AGREGADA: Confirmación de éxito (temporal)
        alert(`¡Compra exitosa! Nuevo saldo disponible.`); 
        
    } catch (error) {
        // La acción de Pinia ya maneja el alert con el error (ej: saldo insuficiente),
        // así que aquí solo dejamos el console.error de respaldo.
        console.error("Fallo la transacción en KioscoComponent.");
    }
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