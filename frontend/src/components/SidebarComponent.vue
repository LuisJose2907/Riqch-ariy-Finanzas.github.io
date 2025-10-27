<script setup>
import { useSessionStore } from '@/stores/sessionStore'; 
import { computed } from 'vue';

const sessionStore = useSessionStore();
const inventarioResumen = computed(() => sessionStore.inventarioTotal); 
</script>

<template>
  <aside class="kiosco-status-panel p-6 rounded-2xl shadow-2xl w-full flex flex-col gap-6">
    
    <div class="stat-card stat-card-saldo">
      <p class="text-sm text-gray-700 font-semibold">💰 Saldo Actual</p>
      <p class="stat-value">{{ sessionStore.saldoFormateado }}</p> 
    </div>

    <div class="stat-card stat-card-inventario">
      <p class="text-sm text-gray-700 font-semibold">📦 Inventario (Productos)</p>
      <ul class="mt-3 text-base space-y-2">
        <li v-for="(stock, name) in inventarioResumen" :key="name" class="inventory-item">
          <span class="text-lg">🛒</span> 
          <span class="font-medium text-gray-800">{{ name }}</span>: 
          <span class="font-bold text-blue-600">{{ stock }} und.</span>
        </li>
        <li v-if="Object.keys(inventarioResumen).length === 0" class="text-gray-500 italic">
            Aún no hay productos en stock.
        </li>
      </ul>
    </div>
  </aside>
</template>

<style scoped>
/* Contenedor principal de la tarjeta de estatus */
.kiosco-status-panel {
    background: white;
    /* Borde superior de marca, similar a las tarjetas de la landing */
    border-top: 5px solid #FF6B6B; /* Rojo/Naranja de la marca */
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
}

/* Estilo para las tarjetas internas de Saldo/Inventario */
.stat-card {
    background: #f7f9fb; /* Un gris muy sutil */
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.05); /* Sombra interna sutil */
    border-left: 5px solid;
    transition: transform 0.2s;
}

.stat-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

/* Estilos específicos por tarjeta para color de borde */
.stat-card-saldo {
    border-left-color: #27ae60; /* Verde (para Saldo/Ganancia) */
}
.stat-card-inventario {
    border-left-color: #3498db; /* Azul (para Inventario/Stock) */
}

/* Estilo del valor clave (Saldo) para usar el degradado de marca */
.stat-value {
    font-size: 3rem;
    font-weight: 900;
    margin-top: 0.25rem;
    /* Aplicamos el degradado de marca (similar al Hero H1) */
    background: linear-gradient(135deg, #FF6B6B 0%, #FFA500 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.inventory-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
</style>