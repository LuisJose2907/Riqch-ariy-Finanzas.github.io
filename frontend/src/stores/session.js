// frontend/src/stores/session.js
import { defineStore } from 'pinia';
import axios from 'axios'; 

// Definir la URL base de la API
const API_BASE_URL = import.meta.env.VITE_APP_API_URL; 

export const useSessionStore = defineStore('session', {
    state: () => ({
        // --- ESTADO DE AUTENTICACIÓN ---
        userRole: 'student', 
        isLoggedIn: false,
        token: null,
        user: null,

        // --- ESTADO DEL SIMULADOR (CRUCIAL PARA SIDEBAR/KIOSCO) ---
        contextoRegional: { region: null, age_stage: null }, // API 1
        productos: [],                                      // API 2
        saldo: 0,                                           // API 5
        inventario: []                                      // API 5
    }),
    
    actions: {
        // --- ACCIONES DEL SIMULADOR ---
        
        // 1. Guarda el contexto regional (Llamada por fetchInitialData en App.vue, API 1)
        setContexto(data) {
            this.contextoRegional = data;
        },

        // 2. Guarda la lista de productos (Llamada por fetchInitialData en App.vue, API 2)
        setProductos(data) {
            this.productos = data;
        },

        // 3. 🎯 CRUCIAL: Obtiene las estadísticas del usuario (Llamada por recargarTodo en App.vue, API 5)
        async fetchUserStats() {
            if (!API_BASE_URL) return console.error("API URL no definida.");

            try {
                // Llama al endpoint de la API 5 para obtener saldo e inventario
                const response = await axios.get(`${API_BASE_URL}/usuario/stats`);
                
                // Actualizar el estado del Sidebar
                this.saldo = response.data.saldo || 0;
                this.inventario = response.data.inventario || [];
                
                console.log("Stats de Usuario (API 5) actualizadas.");

            } catch (error) {
                console.error("Error al cargar estadísticas de usuario (API 5):", error);
            }
        },
        
        // --- ACCIONES DE AUTENTICACIÓN ---
        async login(email, password) {
            // ... (Lógica de Login actual: mantiene userRole, isLoggedIn, etc.)
            const roleFromAPI = email.includes('profesor') ? 'professor' : 'student';

            this.userRole = roleFromAPI; 
            this.isLoggedIn = true;
            this.token = 'fake_jwt_token';
            
            // Opcional: Llamar a fetchUserStats aquí si el login es exitoso
            if (roleFromAPI === 'student') {
                 this.fetchUserStats(); 
            }
            return true; 
        },

        logout() {
            // ... (Lógica de Logout actual)
            this.userRole = 'student';
            this.isLoggedIn = false;
            this.token = null;
            this.user = null;
            
            // Limpiar estado del simulador al cerrar sesión
            this.saldo = 0;
            this.inventario = [];
            this.contextoRegional = { region: null, age_stage: null };
            this.productos = [];
        }
    },
});