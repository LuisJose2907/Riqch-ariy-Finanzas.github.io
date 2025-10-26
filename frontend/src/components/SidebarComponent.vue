<template>
  <aside class="bg-blue-900 text-white p-6 shadow-xl lg:w-64 w-full flex flex-col lg:flex-none">
    
    <div class="mb-8">
      <h2 class="text-2xl font-extrabold border-b border-blue-700 pb-2">
        Estado de la Sesión
      </h2>
    </div>

    <div class="mb-6 bg-blue-800 p-3 rounded-lg">
      <p class="text-sm text-blue-300">Saldo Actual</p>
      <p class="text-3xl font-bold">S/ 500.00</p>
    </div>

    <div class="mb-6 bg-blue-800 p-3 rounded-lg">
      <p class="text-sm text-blue-300">Inventario (Productos)</p>
      <ul class="mt-2 text-sm space-y-1">
        <li>🛒 Bebidas: 10 und.</li>
        <li>🍫 Snacks: 5 und.</li>
      </ul>
    </div>

    <nav class="flex-grow">
      <ul class="space-y-2">
        <li>
          <router-link 
            to="/" 
            class="flex items-center p-3 rounded-lg hover:bg-blue-700 transition"
            active-class="bg-blue-700 font-semibold"
          >
            🛒 Mi Kiosco Local
          </router-link>
        </li>
        <li>
          <router-link 
            to="/chatbot" 
            class="flex items-center p-3 rounded-lg hover:bg-blue-700 transition"
            active-class="bg-blue-700 font-semibold"
          >
            💬 Chatbot YACHAQ
          </router-link>
        </li>
      </ul>
    </nav>
    </aside>
</template>

<script setup>
// Lógica futura para leer el estado del store (Pinia) irá aquí.
</script>