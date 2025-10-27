<script setup>
import { onMounted } from 'vue';
import StudentCard from '@/components/StudentCard.vue';
// 1. Importar el store y Axios (si no está ya en el store)
import { useSessionStore } from '@/stores/session'; 

// Instanciar el store para usar sus estados y acciones
const sessionStore = useSessionStore();

// 2. Usar onMounted para llamar a la API al inicio (Tarea B)
onMounted(() => {
    console.log("Activando carga de progreso de la clase...");
    // Esta acción llama a la API GET /profesor/progreso_clase
    sessionStore.fetchStudentProgress(); 
});

// 3. Función para manejar la adaptación (Tarea C)
const handleAdaptation = (studentId, adjustmentType) => {
    console.log(`Comando recibido en el Dashboard: Estudiante ${studentId}, Tipo de Ajuste: ${adjustmentType}`);
    
    // Aquí se llama a la acción de Pinia para la API POST /profesor/ajustar_nivel
    sessionStore.adjustStudentLevel(studentId, adjustmentType);
};
</script>

<template>
    <div class="professor-dashboard p-6">
        <h1 class="text-4xl font-extrabold text-blue-900 mb-8">
            Panel de Control del Profesor 👨‍🏫
        </h1>
        <p class="text-gray-600 mb-6">
            Monitoreo Rápido y Simple (MARS): Semáforos de Rentabilidad.
        </p>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            
            <StudentCard
                v-for="student in sessionStore.students"
                :key="student.id"
                :student="student"
                @adjust="handleAdaptation" />
            
            <div v-if="!sessionStore.students || sessionStore.students.length === 0" 
                 class="col-span-full text-center py-10 text-gray-500 italic">
                 Cargando datos de la clase desde el servidor... 🔄
            </div>
        </div>
    </div>
</template>

<style scoped>
/* Estilos si son necesarios */
</style>