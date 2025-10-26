<template>
  <div class="max-w-md mx-auto p-8 bg-white rounded-xl shadow-2xl">
    <h1 class="text-3xl font-bold text-blue-900 mb-8 text-center">Registro de Usuario</h1>
    
    <form @submit.prevent>
        <div class="mb-4">
            <label for="username" class="block text-sm font-medium text-gray-700">Nombre de Usuario</label>
            <input type="text" id="username" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm p-2 border" required>
        </div>
        <div class="mb-4">
            <label for="email" class="block text-sm font-medium text-gray-700">Correo Electrónico</label>
            <input type="email" id="email" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm p-2 border" required>
        </div>
        <div class="mb-6">
            <label for="password" class="block text-sm font-medium text-gray-700">Contraseña</label>
            <input type="password" id="password" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm p-2 border" required>
        </div>
        <button type="submit" class="w-full bg-green-600 text-white py-2 rounded-md font-semibold hover:bg-green-700 transition">
            Crear Cuenta
        </button>
        
        <p class="mt-4 text-center text-sm text-gray-600">
            ¿Ya tienes cuenta? 
            <router-link to="/login" class="text-blue-600 hover:underline">Inicia Sesión</router-link>
        </p>
    </form>
  </div>
</template>

<script setup>
// Lógica de autenticación futura (API 4) irá aquí
</script>
<style scoped></style>