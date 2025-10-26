<script setup>
import { useSessionStore } from '@/stores/sessionStore'; 
import { computed } from 'vue';

const sessionStore = useSessionStore();
const inventarioResumen = computed(() => sessionStore.inventarioTotal); 
</script>

<template>
  <aside class="bg-blue-900 text-white p-6 shadow-xl lg:w-64 w-full flex flex-col lg:flex-none">
    <div class="mb-6 bg-blue-800 p-3 rounded-lg">
      <p class="text-sm text-blue-300">Saldo Actual</p>
      <p class="text-3xl font-bold">{{ sessionStore.saldoFormateado }}</p> 
    </div>

    <div class="mb-6 bg-blue-800 p-3 rounded-lg">
      <p class="text-sm text-blue-300">Inventario (Productos)</p>
      <ul class="mt-2 text-sm space-y-1">
        <li v-for="(stock, name) in inventarioResumen" :key="name">
          🛒 {{ name }}: {{ stock }} und.
        </li>
        <li v-if="Object.keys(inventarioResumen).length === 0">
            Aún no hay productos en stock.
        </li>
      </ul>
    </div>
    </aside>
</template>
<style scoped></style>