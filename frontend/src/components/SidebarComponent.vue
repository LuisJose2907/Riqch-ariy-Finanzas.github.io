<script setup>
import { useSessionStore } from '@/stores/session'; 
import { computed } from 'vue';

const sessionStore = useSessionStore();

// ✅ Computed locales de respaldo (por si no existen en el store)
const inventarioResumen = computed(() => {
  // Si el inventario es un array (por ejemplo [{ nombre: "Arroz", cantidad: 5 }])
  if (Array.isArray(sessionStore.inventario)) {
    const resumen = {};
    for (const item of sessionStore.inventario) {
      if (item.nombre && item.cantidad != null) {
        resumen[item.nombre] = item.cantidad;
      }
    }
    return resumen;
  }
  // Si ya es un objeto
  return sessionStore.inventario || {};
});

const saldoFormateado = computed(() =>
  (sessionStore.saldo ?? 0).toLocaleString('es-PE', { style: 'currency', currency: 'PEN' })
);
</script>

<template>
  <aside class="kiosco-status-panel p-6 rounded-2xl shadow-2xl w-full flex flex-col gap-6">
    
    <!-- 💰 Saldo actual -->
    <div class="stat-card stat-card-saldo">
      <p class="text-sm text-gray-700 font-semibold">💰 Saldo Actual</p>
      <p class="stat-value">{{ saldoFormateado }}</p> 
    </div>

    <!-- 📦 Inventario -->
    <div class="stat-card stat-card-inventario">
      <p class="text-sm text-gray-700 font-semibold">📦 Inventario (Productos)</p>
      <ul class="mt-3 text-base space-y-2">
        <li
          v-for="(stock, name) in inventarioResumen"
          :key="name"
          class="inventory-item"
        >
          <span class="text-lg">🛒</span> 
          <span class="font-medium text-gray-800">{{ name }}</span>: 
          <span class="font-bold text-blue-600">{{ stock }} und.</span>
        </li>

        <li
          v-if="Object.keys(inventarioResumen).length === 0"
          class="text-gray-500 italic"
        >
          Aún no hay productos en stock.
        </li>
      </ul>
    </div>
  </aside>
</template>

<style scoped>
.kiosco-status-panel {
  background: white;
  border-top: 5px solid #FF6B6B;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
}

.stat-card {
  background: #f7f9fb;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.05);
  border-left: 5px solid;
  transition: transform 0.2s;
}

.stat-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.stat-card-saldo {
  border-left-color: #27ae60;
}
.stat-card-inventario {
  border-left-color: #3498db;
}

.stat-value {
  font-size: 3rem;
  font-weight: 900;
  margin-top: 0.25rem;
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
