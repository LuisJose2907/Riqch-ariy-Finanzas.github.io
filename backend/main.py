# main.py - Backend del Simulador "Mi Kiosco Escolar" y Chatbot YACHAQ
# Este archivo contiene la lógica de negocio y las definiciones de API.

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
import json
import os
import httpx # Necesario para simular la llamada a la IA

# --- Configuración de la IA ---
# Se utiliza el modelo gemini-2.5-flash-preview-09-2025 para las interacciones del chatbot YACHAQ.
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "") 
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent"
# -----------------------------

# --- Definición de Modelos Pydantic (Usado por FastAPI) ---

class Product(BaseModel):
    id: int
    name: str
    stage: str = Field(description="Etapa pedagógica: Brote (8-9), Tallo (10-11), Fruto (12+)")
    base_cost: float = Field(description="Costo base de adquisición (sin variaciones de mercado)")
    base_price: float = Field(description="Precio base de venta al público (sin variaciones de mercado)")
    inventory: int = Field(description="Cantidad actual en inventario")
    local_demand: str = Field(description="Demanda local: Alta, Media, Baja")
    description: str = Field(description="Descripción pedagógica del producto")

class KioscoState(BaseModel):
    region: str = Field(description="Región actual del simulador (ej: Lima, Cusco)")
    saldo: float = Field(description="Dinero disponible (capital de trabajo)")
    products: List[Product]
    pedagogical_focus: str = Field(description="El foco pedagógico de la sesión (ej: ahorro, riesgo, competencia)")

class ChatRequest(BaseModel):
    history: List[Dict[str, str]] = Field(description="Historial completo de la conversación (role: user/model, text: ...)")
    kiosco_state: KioscoState = Field(description="Estado actual del kiosco para contextualizar la respuesta del IA")
    user_query: str = Field(description="Mensaje nuevo del usuario")
    region: str = Field(description="Región actual para contextualización (ej: Cusco)")

class ChatResponse(BaseModel):
    response_text: str
    is_pedagogical: bool
    source_citations: List[Dict[str, str]] = Field(default_factory=list, description="Citas si se usa búsqueda web")

# --- Datos Iniciales (Declarados directamente para evitar FileNotFoundError) ---

initial_state_lima = KioscoState(
    region="Lima",
    saldo=50.0,
    products=[
        Product(id=1, name="Jugo de caja", stage="Brote", base_cost=2.0, base_price=3.5, inventory=10, local_demand="Media", description="Bebida refrescante, fuente de vitaminas."),
        Product(id=2, name="Chocolates", stage="Brote", base_cost=1.5, base_price=2.5, inventory=15, local_demand="Alta", description="Dulce popular, alta demanda en recreos."),
        Product(id=3, name="Frutas", stage="Tallo", base_cost=1.0, base_price=2.0, inventory=20, local_demand="Baja", description="Opción saludable, baja demanda si no se promociona."),
    ],
    pedagogical_focus="ahorro"
)

initial_state_cusco = KioscoState(
    region="Cusco",
    saldo=75.0,
    products=[
        Product(id=1, name="Agua embotellada", stage="Tallo", base_cost=1.5, base_price=3.0, inventory=15, local_demand="Alta", description="Esencial debido a la altitud."),
        Product(id=2, name="Barra energética", stage="Fruto", base_cost=3.0, base_price=5.0, inventory=10, local_demand="Media", description="Popular entre turistas y deportistas."),
    ],
    pedagogical_focus="riesgo"
)

# Simulación de estados de juego por región (para un juego de un solo usuario)
current_kiosco_state: Dict[str, KioscoState] = {
    "Lima": initial_state_lima,
    "Cusco": initial_state_cusco
}

# --- Inicialización y Configuración de FastAPI ---

app = FastAPI(
    title="Backend Riqch'ariy Finanzas (P2)",
    description="APIs para el simulador 'Mi Kiosco Escolar' y el chatbot pedagógico YACHAQ.",
    version="1.0.0"
)

# Configuración CORS: Permite que el Frontend (cualquier origen) acceda a este Backend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

# --- Funciones Auxiliares (Comunicación con IA) ---

async def call_gemini_api(payload: dict, chat_data: ChatRequest) -> Dict:
    """Función para llamar a la API de Gemini con manejo de errores y reintentos."""
    if not GEMINI_API_KEY:
        # Esto es un MOCK de respuesta para la prueba, ya que no tienes la clave API configurada
        print("ADVERTENCIA: Usando respuesta simulada de IA. GEMINI_API_KEY no configurada.")
        
        # Obtenemos el saldo y foco del contexto
        saldo_actual = chat_data.kiosco_state.saldo
        foco_actual = chat_data.kiosco_state.pedagogical_focus
        region_actual = chat_data.region
        
        mock_text = f"¡Hola! Soy YACHAQ, un tutor IA en la región de {region_actual}. Tienes un saldo de S/{saldo_actual:.2f}. Tu foco de la sesión es '{foco_actual}'. Sobre tu pregunta ('{chat_data.user_query}'), te recomiendo pensar en el {foco_actual} antes de tomar decisiones. [MOCK RESPONSE]"
        
        return {
            "candidates": [{
                "content": {
                    "parts": [{"text": mock_text}]
                }
            }]
        }

    # Lógica para llamada real (comentada porque la clave no está disponible localmente)
    # try:
    #     async with httpx.AsyncClient() as client:
    #         api_url_with_key = f"{GEMINI_API_URL}?key={GEMINI_API_KEY}"
    #         response = await client.post(api_url_with_key, json=payload, headers={"Content-Type": "application/json"})
    #         response.raise_for_status()
    #         return response.json()
    # except Exception as e:
    #     print(f"Error al llamar a la API de Gemini: {e}")
    #     return {"error": f"Error de conexión con la IA: {e}"}
    
def build_gemini_payload(chat_data: ChatRequest) -> dict:
    """Construye el payload para la API de Gemini, incluyendo el System Instruction."""

    # 1. System Instruction: Define el rol de YACHAQ y el contexto pedagógico.
    system_instruction = f"""
    Actúa como YACHAQ, un chatbot tutor pedagógico y experto en el juego 'Mi Kiosco Escolar'.
    Tu objetivo es guiar a un niño en la Etapa {chat_data.kiosco_state.products[0].stage} (8-12 años) en temas de finanzas básicas.
    El foco pedagógico actual es '{chat_data.kiosco_state.pedagogical_focus}'.
    Siempre debes contextualizar tu respuesta usando la región actual: {chat_data.region}.

    Instrucciones clave:
    1. Responde de manera amigable, alentadora y usando un lenguaje simple.
    2. Utiliza la información del estado del kiosco para dar consejos relevantes.
    3. NO menciones directamente los detalles técnicos (Pydantic, Python, FastAPI).
    4. El estado actual del kiosco es: Saldo S/{chat_data.kiosco_state.saldo}. Productos: {[(p.name, p.inventory) for p in chat_data.kiosco_state.products]}.
    5. Si el usuario pregunta algo que no tiene que ver con finanzas, redirige amablemente al tema.
    """

    # 2. Historial de Conversación
    contents = []
    for message in chat_data.history:
        contents.append({"role": message.get("role"), "parts": [{"text": message.get("text")}]})

    # 3. El mensaje nuevo del usuario
    contents.append({"role": "user", "parts": [{"text": chat_data.user_query}]})

    # 4. Construcción final del Payload
    payload = {
        "contents": contents,
        "systemInstruction": {
            "parts": [{"text": system_instruction}]
        },
    }
    return payload


# --- Endpoints de la API ---

@app.get("/status")
def get_status():
    """Endpoint de salud para verificar que el servicio está activo."""
    return {"status": "ok", "service": "Backend P2 - Riqch'ariy Finanzas"}

@app.get("/geo/context/{region}", response_model=KioscoState)
async def get_kiosco_state(region: str):
    """API 1: Retorna el estado inicial del kiosco para una región específica."""
    if region in current_kiosco_state:
        # Se devuelve directamente el objeto KioscoState que está correctamente tipado
        return current_kiosco_state[region]
    raise HTTPException(status_code=404, detail=f"Región '{region}' no encontrada.")

@app.post("/transaction/buy", response_model=KioscoState)
async def buy_products(region: str, product_id: int, quantity: int):
    """API 2: Procesa la compra de productos, actualizando el inventario y el saldo."""
    if region not in current_kiosco_state:
        raise HTTPException(status_code=404, detail=f"Región '{region}' no encontrada.")

    state = current_kiosco_state[region]
    product = next((p for p in state.products if p.id == product_id), None)

    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado.")
    if quantity <= 0:
        raise HTTPException(status_code=400, detail="La cantidad debe ser positiva.")

    cost = product.base_cost * quantity
    if state.saldo < cost:
        raise HTTPException(status_code=400, detail="Saldo insuficiente para la compra.")

    # Ejecutar la transacción
    state.saldo -= cost
    product.inventory += quantity
    # current_kiosco_state[region] ya está actualizado (se pasa por referencia)
    return state

@app.post("/transaction/sell", response_model=KioscoState)
async def sell_products(region: str, product_id: int, quantity: int):
    """API 3: Procesa la venta de productos, actualizando el saldo y el inventario."""
    if region not in current_kiosco_state:
        raise HTTPException(status_code=404, detail=f"Región '{region}' no encontrada.")

    state = current_kiosco_state[region]
    product = next((p for p in state.products if p.id == product_id), None)

    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado.")
    if quantity <= 0:
        raise HTTPException(status_code=400, detail="La cantidad debe ser positiva.")
    if product.inventory < quantity:
        raise HTTPException(status_code=400, detail="Inventario insuficiente para la venta.")

    # Ejecutar la transacción
    revenue = product.base_price * quantity
    state.saldo += revenue
    product.inventory -= quantity
    # current_kiosco_state[region] ya está actualizado (se pasa por referencia)
    return state


@app.post("/ia/chat", response_model=ChatResponse)
async def chat_with_yachaq(chat_data: ChatRequest):
    """API 4: Permite interactuar con el chatbot YACHAQ, contextualizado con el estado del kiosco."""

    # 1. Construir el payload con el contexto
    payload = build_gemini_payload(chat_data)

    # 2. Llamar a la API de Gemini (se usa un mock de respuesta si no hay clave)
    gemini_response = await call_gemini_api(payload, chat_data)
    
    if "error" in gemini_response:
        raise HTTPException(status_code=500, detail=gemini_response["error"])

    # 3. Procesar la respuesta
    try:
        text_response = gemini_response["candidates"][0]["content"]["parts"][0]["text"]
        
        return ChatResponse(
            response_text=text_response,
            is_pedagogical=True, # Por defecto es pedagógico
            source_citations=[]
        )
    except (KeyError, IndexError):
        raise HTTPException(status_code=500, detail="Respuesta inesperada o incompleta de la IA.")

@app.post("/ia/reto-sol", response_model=KioscoState) # Cambiamos la respuesta a KioscoState para reflejar el cambio
async def execute_reto_del_sol(region: str):
    """API 5: Ejecuta la funcionalidad avanzada 'El Reto del Sol' con la IA."""
    
    if region not in current_kiosco_state:
        raise HTTPException(status_code=404, detail=f"Región '{region}' no encontrada.")
        
    state = current_kiosco_state[region]
    
    # -----------------------------------------------------
    # LÓGICA DEL EVENTO (Ejecutado por el Backend, no la IA)
    # -----------------------------------------------------
    
    event_message = ""
    
    if region == "Lima":
        # Evento en Lima: Aumenta la demanda y el saldo
        event_message = "¡Reto del Sol: Un evento deportivo en Lima ha disparado la demanda de jugos de caja! ¡Ventas extra!"
        product_id_jugo = 1 # ID del jugo de caja
        product = next((p for p in state.products if p.id == product_id_jugo), None)
        
        if product and product.inventory >= 5:
            state.saldo += product.base_price * 5
            product.inventory -= 5
        elif product:
            event_message = "¡Reto del Sol! Un gran evento falló: ¡No tenías suficiente stock de jugos de caja! Pierdes S/5.00 en oportunidades."
            state.saldo -= 5.0

    elif region == "Cusco":
        # Evento en Cusco: Pequeña ganancia inesperada (turismo)
        event_message = "¡Reto del Sol: Un turista ha pagado extra por una barra energética! Ganancia inesperada."
        state.saldo += 5.0
    
    # Después de la lógica, actualizamos el mensaje de la región (temporalmente para mostrar el resultado)
    state.pedagogical_focus = event_message
    
    # En un entorno real, la IA generaría la narrativa, pero aquí el Backend ejecuta la lógica
    return state
