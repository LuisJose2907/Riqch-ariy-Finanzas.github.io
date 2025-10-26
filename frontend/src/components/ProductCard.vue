<script setup>
defineProps({
  product: Object
});
// Asegúrate de definir el evento 'buy'
const emit = defineEmits(['buy']); 
</script>

<template>
  <div class="bg-white p-4 rounded-lg shadow hover:shadow-lg transition">
    <h3 class="text-xl font-bold text-blue-900">{{ product.nombre }}</h3>
    <p class="text-gray-600 mb-4">{{ product.descripcion }}</p>

    <button 
        @click="$emit('buy', product.id)" 
        class="bg-green-500 text-white p-2 rounded hover:bg-green-600 transition disabled:opacity-50"
    >
      Comprar (S/ {{ product.precio }})
    </button>
  </div>
</template>