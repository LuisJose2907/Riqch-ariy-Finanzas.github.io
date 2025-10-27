<script setup>
// Definimos las propiedades que esta tarjeta recibirá del Dashboard principal.
defineProps({
    student: {
        type: Object,
        required: true,
        // Ejemplo de estructura de datos: 
        // { id: 1, name: 'Juan Pérez', level: 'Etapa Brote', rentability: 0.78 }
    }
});

// Esta función se usa para determinar el color de semaforización
const getRentabilityColor = (rentability) => {
    if (rentability >= 0.8) return 'bg-green-500'; // Verde: > 80% (Maestría)
    if (rentability >= 0.6) return 'bg-yellow-500'; // Amarillo: 60%-80% (Requiere Observación)
    return 'bg-red-500'; // Rojo: < 60% (Requiere Refuerzo)
};
</script>

<template>
    <div class="
        bg-white p-5 rounded-lg shadow-lg border-l-4 border-blue-500 
        hover:shadow-xl transition duration-300 flex flex-col justify-between
    ">
        <div class="mb-4">
            <h3 class="text-xl font-bold text-gray-800 mb-1">
                {{ student.name }}
            </h3>
            
            <span class="
                bg-blue-100 text-blue-800 text-sm font-semibold 
                px-3 py-1 rounded-full inline-block
            ">
                Nivel Actual: {{ student.level }}
            </span>
        </div>

        <div class="flex items-center justify-between mb-5 border-t border-b py-3">
            <div class="text-sm text-gray-600">
                Rentabilidad Promedio
            </div>
            
            <div :class="getRentabilityColor(student.rentability)" 
                 class="w-10 h-10 rounded-full flex items-center justify-center text-white font-bold text-xs shadow-md">
                {{ (student.rentability * 100).toFixed(0) }}%
            </div>
        </div>

        <div class="flex space-x-3">
            <button class="
                flex-1 bg-indigo-500 text-white py-2 rounded-lg text-sm font-semibold 
                hover:bg-indigo-600 transition
            ">
                ⬆️ Ajustar Dificultad
            </button>
            
            <button class="
                flex-1 bg-red-500 text-white py-2 rounded-lg text-sm font-semibold 
                hover:bg-red-600 transition
            ">
                📚 Asignar Refuerzo
            </button>
        </div>
    </div>
</template>

<style scoped>
/* Estilos específicos si son necesarios */
</style>