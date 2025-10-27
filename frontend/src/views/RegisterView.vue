<template>
  <div class="register-body-wrapper">
    <div class="register-container">
      <h1 class="register-title">Únete a Riqch'ariy</h1>
      <p class="register-subtitle">Crea tu cuenta para empezar a sembrar prosperidad.</p>

      <form @submit.prevent="handleRegister" id="registerForm">
        
        <div class="form-section">
          <label class="section-label">1. ¿Cuál es tu rol principal?</label>
          <div class="role-selection-grid">
            
            <div 
              class="role-card" 
              :class="{ 'selected': selectedRole === 'adulto' }" 
              @click="selectedRole = 'adulto'"
            >
              <div class="role-icon">👨‍👩‍👧‍👦</div>
              <h3>Adulto / Padre</h3>
              <p>Gestionar la cuenta familiar y acompañar el proceso.</p>
            </div>
            
            <div 
              class="role-card" 
              :class="{ 'selected': selectedRole === 'estudiante' }" 
              @click="selectedRole = 'estudiante'"
            >
              <div class="role-icon">🎒</div>
              <h3>Estudiante / Hijo</h3>
              <p>Acceder a los módulos interactivos y simuladores.</p>
            </div>
          </div>
        </div>

        <div class="form-section">
          <label class="section-label">2. Crea tus credenciales</label>
          
          <div class="input-group">
            <label for="email">Correo Electrónico</label>
            <input type="email" id="email" v-model="form.email" required>
          </div>
          
          <div class="input-group">
            <label for="password">Contraseña</label>
            <input type="password" id="password" v-model="form.password" @input="updatePasswordStrength" required>
            <div class="strength-bar-container">
              <div :class="['strength-bar-fill', strengthClass]" :style="{ width: strengthWidth }"></div>
            </div>
            <span class="strength-text">{{ strengthText }}</span>
          </div>
        </div>

        <div class="form-section">
          <label class="section-label">3. Datos de Contexto</label>
          
          <div class="input-group">
            <label for="region">Región donde vive el estudiante</label>
            <select id="region" v-model="form.region" required>
              <option value="" disabled>Selecciona una región</option>
              <option value="lima">Lima</option>
              <option value="cusco">Cusco</option>
              <option value="arequipa">Arequipa</option>
              <option value="piura">Piura</option>
              <option value="la_libertad">La Libertad</option>
              <option value="otro">Otra (Adaptación Contextual)</option>
            </select>
          </div>
        </div>

        <button type="submit" class="submit-button">
          Crear Cuenta Ahora 🚀
        </button>
        
        <p class="login-link">
          ¿Ya tienes cuenta? 
          <router-link to="/login" class="text-blue-600 font-semibold hover:underline">Inicia Sesión</router-link>
        </p>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const selectedRole = ref(null);

const form = ref({
  email: '',
  password: '',
  region: '',
});

// Lógica de Medidor de Contraseña (Simplificada para el Frontend)
const strength = ref(0); // 0: Muy Débil, 4: Fuerte
const strengthText = computed(() => {
  if (strength.value === 0) return 'Muy Débil';
  if (strength.value === 1) return 'Débil';
  if (strength.value === 2) return 'Medio';
  if (strength.value === 3) return 'Fuerte';
  if (strength.value === 4) return 'Muy Fuerte';
  return 'Muy Débil';
});

const strengthWidth = computed(() => {
  return `${(strength.value / 4) * 100}%`;
});

const strengthClass = computed(() => {
  if (strength.value === 0 || strength.value === 1) return 'strength-weak';
  if (strength.value === 2) return 'strength-medium';
  if (strength.value === 3 || strength.value === 4) return 'strength-strong';
  return '';
});

const updatePasswordStrength = () => {
  const value = form.value.password;
  let s = 0;
  
  if (value.length >= 8) s++;
  if (value.match(/[a-z]/) && value.match(/[A-Z]/)) s++;
  if (value.match(/[0-9]/)) s++;
  if (value.match(/[^a-zA-Z0-9]/)) s++;
  
  strength.value = s;
};

const handleRegister = () => {
  if (!selectedRole.value || !form.value.region) {
    alert('Por favor, selecciona un rol y una región.');
    return;
  }
  // Lógica futura de API 4 (Registro) va aquí
  console.log('Datos de Registro:', { ...form.value, role: selectedRole.value });
  alert('¡Registro simulado exitoso! Se enviaría a la API de Autenticación.');
};
</script>

<style>
/* ------------------ ESTILOS GLOBALES DE REGISTRO (NO SCOPED) ------------------ */

/* Replica el fondo animado del HTML original, es fundamental para el diseño */
.register-body-wrapper {
  /* Fondo Degradado Animado */
  background: linear-gradient(135deg, #FF6B6B 0%, #4ECDC4 50%, #FFE66D 100%);
  background-size: 400% 400%;
  animation: gradientShift 8s ease infinite;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 4rem 2rem;
  position: relative;
  overflow-x: hidden;
  color: #2c3e50;
}

@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* Estrellas decorativas (para simular el efecto del HTML) */
.register-body-wrapper::before {
  content: '⭐🌟✨💫🎯🚀🎈🎉⭐🌟✨💫🎯🚀🎈🎉⭐🌟✨💫🎯🚀🎈🎉';
  position: absolute;
  font-size: 3rem;
  top: 0;
  left: -10%;
  width: 120%;
  opacity: 0.3;
  white-space: nowrap;
  animation: floatStars 20s linear infinite;
  z-index: 0;
}

@keyframes floatStars {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}


/* ------------------ CONTENEDOR PRINCIPAL ------------------ */

.register-container {
  background: white;
  padding: 3rem;
  border-radius: 20px;
  box-shadow: 0 15px 50px rgba(0, 0, 0, 0.4);
  max-width: 600px;
  width: 100%;
  z-index: 10;
  border-top: 5px solid #FF6B6B;
}

.register-title {
  font-size: 2.5rem;
  color: #2c3e50;
  text-align: center;
  margin-bottom: 0.5rem;
  font-weight: 800;
}

.register-subtitle {
  text-align: center;
  color: #7f8c8d;
  font-size: 1.1rem;
  margin-bottom: 2rem;
}

/* ------------------ SECCIONES DE FORMULARIO ------------------ */

.form-section {
  margin-bottom: 2rem;
  padding: 1.5rem 0;
  border-bottom: 1px dashed #eee;
}

.section-label {
  display: block;
  font-size: 1.25rem;
  font-weight: 700;
  color: #34495e;
  margin-bottom: 1rem;
}

/* ------------------ SELECCIÓN DE ROL ------------------ */

.role-selection-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}

.role-card {
  background: #f7f9fb;
  border: 2px solid #ddd;
  padding: 1.5rem;
  border-radius: 15px;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
}

.role-card:hover {
  border-color: #4ECDC4;
  box-shadow: 0 6px 20px rgba(78, 205, 196, 0.2);
}

.role-card.selected {
  background: #E0F7F5; /* Fondo más claro y juguetón */
  border-color: #4ECDC4;
  box-shadow: 0 8px 30px rgba(78, 205, 196, 0.4);
  transform: translateY(-5px);
}

.role-icon {
  font-size: 3rem;
  margin-bottom: 0.5rem;
}

.role-card h3 {
  font-size: 1.2rem;
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 0.3rem;
}

.role-card p {
  font-size: 0.9rem;
  color: #7f8c8d;
}

/* ------------------ INPUTS ------------------ */

.input-group {
  margin-bottom: 1.5rem;
}

.input-group label {
  display: block;
  font-size: 0.95rem;
  font-weight: 500;
  color: #34495e;
  margin-bottom: 0.5rem;
}

.input-group input,
.input-group select {
  width: 100%;
  padding: 0.8rem 1rem;
  border: 1px solid #ddd;
  border-radius: 10px;
  font-size: 1rem;
  transition: border-color 0.3s, box-shadow 0.3s;
}

.input-group input:focus,
.input-group select:focus {
  border-color: #4ECDC4;
  box-shadow: 0 0 0 3px rgba(78, 205, 196, 0.3);
  outline: none;
}

/* ------------------ MEDIDOR DE FUERZA ------------------ */

.strength-bar-container {
  background: #f0f0f0;
  height: 8px;
  border-radius: 4px;
  margin-top: 0.5rem;
  overflow: hidden;
}

.strength-bar-fill {
  height: 100%;
  transition: width 0.3s ease-in-out, background-color 0.3s;
}

.strength-weak {
  background-color: #e74c3c; /* Rojo */
}

.strength-medium {
  background-color: #f39c12; /* Naranja */
}

.strength-strong {
  background-color: #27ae60; /* Verde */
}

.strength-text {
  display: block;
  margin-top: 0.5rem;
  font-size: 0.8rem;
  color: #7f8c8d;
}

/* ------------------ BOTÓN DE ENVÍO ------------------ */

.submit-button {
  width: 100%;
  background: linear-gradient(135deg, #FF6B6B 0%, #FFA500 100%);
  color: white;
  padding: 1rem;
  border: none;
  border-radius: 15px;
  font-size: 1.3rem;
  font-weight: 800;
  cursor: pointer;
  transition: transform 0.3s, box-shadow 0.3s;
  box-shadow: 0 6px 20px rgba(255, 107, 107, 0.4);
}

.submit-button:hover {
  transform: translateY(-3px) scale(1.01);
  box-shadow: 0 10px 25px rgba(255, 107, 107, 0.6);
}

.login-link {
  text-align: center;
  margin-top: 1.5rem;
  font-size: 0.95rem;
}

/* Media Query para móvil */
@media (max-width: 500px) {
  .register-container {
    padding: 2rem;
  }
  .role-selection-grid {
    grid-template-columns: 1fr;
  }
}
</style>