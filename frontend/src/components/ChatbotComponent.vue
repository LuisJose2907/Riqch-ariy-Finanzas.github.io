<template>
  <div class="chatbot-container max-w-4xl mx-auto h-[80vh] flex flex-col bg-white rounded-3xl shadow-2xl border-t-8 border-green-500 overflow-hidden">
    
    <header class="p-6 border-b border-gray-100 flex items-center bg-gray-50">
      <span class="text-4xl mr-3">🤖</span>
      <div>
        <h2 class="text-2xl font-extrabold text-green-700">
          Chatbot YACHAQ
        </h2>
        <p class="text-sm text-gray-500">
          Tu asistente financiero con IA. Pregúntame sobre tus decisiones.
        </p>
      </div>
    </header>

    <div class="flex-1 p-6 space-y-4 overflow-y-auto">
      
      <div class="flex justify-start">
        <div class="ia-message max-w-xs md:max-w-md p-3">
          ¡Hola! Soy YACHAQ, un placer ayudarte. ¿Tienes preguntas sobre tus compras, presupuesto o cómo ahorrar?
        </div>
      </div>

      <div class="flex justify-end">
        <div class="user-message max-w-xs md:max-w-md p-3">
          ¿Cuál es la mejor manera de invertir mis ahorros en Perú?
        </div>
      </div>
      
      <div class="flex justify-start">
        <div class="ia-message max-w-xs md:max-w-md p-3 bg-yellow-50 border-yellow-300">
          <p class="font-bold text-yellow-700">🔧 MODO DESARROLLO:</p>
          <p class="text-sm text-gray-600 mt-1">
            (La lógica de interacción y la conexión a las APIs de IA (API 4 y 5) aún están pendientes de implementación. Se activarán en la siguiente fase de desarrollo).
          </p>
        </div>
      </div>
    </div>

    <div class="p-4 border-t border-gray-200 bg-white flex items-center gap-3">
      <input 
        type="text" 
        placeholder="Escribe tu pregunta a YACHAQ..." 
        class="flex-1 p-3 border border-gray-300 rounded-full focus:ring-green-500 focus:border-green-500 transition"
        disabled
      >
      <button 
        class="bg-green-600 text-white p-3 rounded-full font-semibold hover:bg-green-700 transition shadow-lg disabled:opacity-50"
        disabled
      >
        Enviar
      </button>
    </div>
  </div>
</template>

<script setup>
// La lógica futura de conexión a la API 4/5 (Chatbot) se añadirá aquí.
</script>

<style scoped>
/* Estilos aplicados para la coherencia estética global */

/* Contenedor principal de la tarjeta del Chatbot */
.chatbot-container {
    /* La base ya está en el template (bg-white, shadow-2xl, border-t-8 border-green-500) */
    position: relative;
}

/* Estilo para los mensajes del usuario */
.user-message {
    /* Aplicamos el color Turquesa/Azul de la marca para el usuario */
    background-color: #4ECDC4; 
    color: white;
    padding: 10px 15px;
    border-radius: 20px 20px 5px 20px; /* Borde de chat 'hablando' */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Estilo para los mensajes de YACHAQ (IA) */
.ia-message {
    /* Fondo muy sutil para el bot, con borde de marca */
    background-color: #f7f9fb; 
    border: 1px solid #eee;
    padding: 10px 15px;
    border-radius: 20px 20px 20px 5px; /* Borde de chat 'escuchando' */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
}
</style>