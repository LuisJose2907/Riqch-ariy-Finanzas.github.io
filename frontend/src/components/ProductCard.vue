<template>
  <div class="bg-white rounded-xl shadow-lg p-5 border border-gray-100 transition-transform hover:shadow-xl">

    <div class="flex justify-between items-start mb-3">
        <h3 class="text-xl font-bold text-gray-800">{{ product.name || 'Producto X' }}</h3>
        <span class="text-sm font-medium px-3 py-1 bg-yellow-100 text-yellow-800 rounded-full">
            Demanda: {{ product.local_demand || 'Media' }}
        </span>
    </div>

    <p class="text-3xl font-extrabold text-green-600 mb-2">S/ {{ product.price ? product.price.toFixed(2) : '0.00' }}</p>
    <p class="text-sm text-gray-500 mb-4">Stock: {{ product.stock || 0 }} unidades</p>

    <button 
      @click="$emit('comprar', product.id)"
      class="w-full py-3 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition disabled:bg-gray-400"
      :disabled="product.stock <= 0"
    >
      Comprar
    </button>
  </div>
</template>

<script setup>
const props = defineProps({
  product: {
    type: Object,
    required: true
  }
})
const emits = defineEmits(['comprar'])
</script>