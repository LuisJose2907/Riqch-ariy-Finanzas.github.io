<template>
  <div class="login-body-wrapper">
    <div class="login-container">
      <div class="login-header">
        <div class="logo-icon">🔑</div>
        <h1 class="login-title">Iniciar Sesión</h1>
        <p class="login-subtitle">Bienvenido de vuelta. ¡Continuemos sembrando prosperidad!</p>
      </div>

      <form @submit.prevent="handleLogin" id="loginForm">
        
        <div class="input-group">
          <label for="email">Correo Electrónico</label>
          <input type="email" id="email" v-model="form.email" required placeholder="tu.correo@riqchariy.com">
        </div>
        
        <div class="input-group mb-8">
          <label for="password">Contraseña</label>
          <input type="password" id="password" v-model="form.password" required placeholder="••••••••">
        </div>
        
        <button type="submit" class="submit-button">
          Ingresar a la Plataforma 🎯
        </button>
      </form>

      <div class="divider">
          <span>O continúa con</span>
      </div>

      <div class="social-login">
          <button class="social-btn google-btn" title="Iniciar con Google">
            <span class="icon">🔍</span> Google
          </button>
          <button class="social-btn facebook-btn" title="Iniciar con Facebook">
            <span class="icon">📘</span> Facebook
          </button>
      </div>
      
      <p class="form-footer-text">
          ¿Aún no tienes una cuenta? 
          <router-link to="/register" class="link-register">Regístrate aquí</router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const form = ref({
  email: '',
  password: '',
});

const handleLogin = () => {
  // Lógica futura de API 4 (Login) va aquí
  console.log('Datos de Login:', form.value);
  alert('¡Login simulado exitoso! Se enviaría a la API de Autenticación.');
};
</script>

<style>
/* ------------------ ESTILOS GLOBALES DE LOGIN (Debe coincidir con RegisterView) ------------------ */

/* Replica el fondo animado del Register y Home */
.login-body-wrapper {
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

/* Reusa el keyframe de RegisterView.vue */
@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* Estrellas decorativas (para simular el efecto del HTML) */
.login-body-wrapper::before {
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


/* ------------------ CONTENEDOR PRINCIPAL DE LOGIN ------------------ */

.login-container {
  background: white;
  padding: 3rem;
  border-radius: 20px;
  box-shadow: 0 15px 50px rgba(0, 0, 0, 0.4);
  max-width: 450px; /* Un poco más estrecho que el Registro */
  width: 100%;
  z-index: 10;
  border-top: 5px solid #4ECDC4; /* Color diferente al Registro */
}

.login-header {
  text-align: center;
  margin-bottom: 2rem;
}

.logo-icon {
  font-size: 3rem;
  margin-bottom: 0.5rem;
}

.login-title {
  font-size: 2.2rem;
  color: #2c3e50;
  margin-bottom: 0.5rem;
  font-weight: 800;
}

.login-subtitle {
  color: #7f8c8d;
  font-size: 1rem;
}

/* ------------------ INPUTS (Reutilizando estilos de Register) ------------------ */

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

.input-group input {
  width: 100%;
  padding: 0.8rem 1rem;
  border: 1px solid #ddd;
  border-radius: 10px;
  font-size: 1rem;
  transition: border-color 0.3s, box-shadow 0.3s;
}

.input-group input:focus {
  border-color: #FF6B6B; /* Color de foco diferente */
  box-shadow: 0 0 0 3px rgba(255, 107, 107, 0.3);
  outline: none;
}

/* ------------------ BOTÓN DE ENVÍO ------------------ */

.submit-button {
  width: 100%;
  /* Degradado de botón de ingreso */
  background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%);
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

/* ------------------ DIVISOR Y SOCIAL LOGIN ------------------ */

.divider {
  display: flex;
  align-items: center;
  text-align: center;
  margin: 2rem 0;
  color: #95a5a6;
}

.divider::before,
.divider::after {
  content: '';
  flex: 1;
  border-bottom: 1px solid #ecf0f1;
}

.divider:not(:empty)::before {
  margin-right: 0.5em;
}

.divider:not(:empty)::after {
  margin-left: 0.5em;
}

.social-login {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}

.social-btn {
  background: #f7f9fb;
  border: 1px solid #ddd;
  padding: 0.8rem 1.5rem;
  border-radius: 10px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  display: flex;
  align-items: center;
}

.social-btn:hover {
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    transform: translateY(-2px);
}

.social-btn .icon {
    margin-right: 0.5rem;
    font-size: 1.2rem;
}

.form-footer-text {
  text-align: center;
  font-size: 0.95rem;
  color: #7f8c8d;
}

.link-register {
  color: #4ECDC4;
  font-weight: 600;
  text-decoration: none;
  transition: color 0.3s;
}

.link-register:hover {
  text-decoration: underline;
  color: #38EF7D;
}

</style>