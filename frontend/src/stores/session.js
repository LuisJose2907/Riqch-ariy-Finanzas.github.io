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

    // 👇 NUEVOS GETTERS (computados globales)
    getters: {
        // Formatea el saldo a moneda peruana
        saldoFormateado: (state) => 
            state.saldo.toLocaleString('es-PE', { style: 'currency', currency: 'PEN' }),

        // Devuelve el inventario como objeto { nombre: cantidad }
        inventarioTotal: (state) => {
            if (!Array.isArray(state.inventario)) return {};
            const resumen = {};
            for (const item of state.inventario) {
                if (item.nombre && item.cantidad) {
                    resumen[item.nombre] = item.cantidad;
                }
            }
            return resumen;
        }
    },
    
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

        // 3. 🎯 Obtiene las estadísticas del usuario (Llamada por recargarTodo en App.vue, API 5)
        async fetchUserStats() {
            if (!API_BASE_URL) return console.error("API URL no definida.");

            try {
                const response = await axios.get(`${API_BASE_URL}/usuario/stats`);
                this.saldo = response.data.saldo || 0;
                this.inventario = response.data.inventario || [];
                console.log("Stats de Usuario (API 5) actualizadas.");
            } catch (error) {
                console.error("Error al cargar estadísticas de usuario (API 5):", error);
            }
        },
        
        // --- ACCIONES DE AUTENTICACIÓN ---
        async login(email, password) {
            const roleFromAPI = email.includes('profesor') ? 'professor' : 'student';

            this.userRole = roleFromAPI; 
            this.isLoggedIn = true;
            this.token = 'fake_jwt_token';
            
            if (roleFromAPI === 'student') {
                this.fetchUserStats(); 
            }
            return true; 
        },

        logout() {
            this.userRole = 'student';
            this.isLoggedIn = false;
            this.token = null;
            this.user = null;
            this.saldo = 0;
            this.inventario = [];
            this.contextoRegional = { region: null, age_stage: null };
            this.productos = [];
        }
    },
});
