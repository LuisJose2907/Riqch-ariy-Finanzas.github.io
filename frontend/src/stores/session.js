// frontend/src/stores/session.js
import { defineStore } from 'pinia';
import axios from 'axios'; 

export const useSessionStore = defineStore('session', {
    state: () => ({
        userRole: 'student', // Estado inicial. Debe ser 'professor' o 'student'.
        isLoggedIn: false,
        token: null,
        user: null,
    }),
    
    actions: {
        // Esta acción simula el proceso de inicio de sesión real
        // Aquí se llamaría a la API de login y se guardaría el rol.
        async login(email, password) {
            try {
                // Simulación de una llamada a la API de login
                // const response = await axios.post('http://localhost:8000/auth/login', { email, password });
                
                // **Simulación de Respuesta Exitosa con Rol**
                const roleFromAPI = email.includes('profesor') ? 'professor' : 'student';

                this.userRole = roleFromAPI; // Guarda el rol para el router guard
                this.isLoggedIn = true;
                this.token = 'fake_jwt_token';
                
                // Si la sesión guarda el rol, la protección de rutas funciona.
                return true; 
            } catch (error) {
                this.logout();
                return false;
            }
        },

        logout() {
            this.userRole = 'student';
            this.isLoggedIn = false;
            this.token = null;
            this.user = null;
            // Opcional: Redirigir al usuario al login tras el cierre
        }
    },
    // Opcional: Puedes usar 'persist: true' si quieres que el estado se guarde en localStorage
});