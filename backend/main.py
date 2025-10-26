from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
import json
import random
from fastapi.middleware.cors import CORSMiddleware 
# --- SYSTEM PROMPT (SIMULACIÓN DE P4) ---
# Este es el texto base que guía a la IA y se inyecta con variables dinámicas.
SYSTEM_PROMPT_TEMPLATE = """
Eres YACHAQ, un tutor financiero andino amigable y sabio. Tu objetivo es educar a un niño de la región de {region}, quien se encuentra en la etapa pedagógica {age_stage} (Brote o Desarrollo).

Reglas:
1. Siempre usa un tono motivador y adaptado al contexto cultural peruano.
2. Basas tus consejos en el contexto del kiosco: saldo, inventario y la región específica.
3. Enfatiza los conceptos pedagógicos clave: Ahorro, Inversión, Riesgo y Competencia.
"""
# --- SETUP INICIAL ---
app = FastAPI(
    title="Riqch'ariy Finanzas - Backend MVP",
    version="1.0.0"
)

# Configuración CORS 
origins = ["http://localhost:5173", "http://localhost:8000", "*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- CARGA DE DATOS ---
def load_data():
    """Carga los datos de productos y eventos desde el archivo JSON de P4."""
    try:
        with open("data/products.json", "r", encoding="utf-8") as f: 
            data = json.load(f)
        return data["products"], data["events"]
    except FileNotFoundError:
        # Esto ocurre si products.json fue creado, pero no guardado con el contenido JSON.
        raise RuntimeError("ERROR: Archivo de datos no encontrado en data/products.json o está vacío.")

PRODUCTS_DATA, RETO_EVENTS = load_data()


# --- MODELOS PYDANTIC ACTUALIZADOS (Nuevos Modelos para IA) ---

# Modelo base para el estado del kiosco
class KioscoState(BaseModel):
    saldo_actual: float = 50.00
    inventario: Dict[str, int] = {} 

# Modelo para API 3 (Transacciones)
class TransactionRequest(BaseModel):
    user_state: KioscoState
    product_name: str
    quantity: int
    is_sale: bool

# Nuevo Modelo para historial de Chat (API 4 y 5)
class ChatMessage(BaseModel):
    role: str # "user" o "assistant"
    content: str

# Nuevo Modelo para API 4: POST /ia/chat
class ChatRequest(BaseModel):
    user_context: KioscoState
    region: str
    age_stage: str
    chat_history: List[ChatMessage]
    new_message: str

# Nuevo Modelo para API 5: POST /ia/feedback
class FeedbackRequest(BaseModel):
    user_context: KioscoState
    region: str
    age_stage: str
    financial_result: float # Positivo para ganancia, negativo para pérdida
    pedagogical_focus: str # Ej: "Fondo de emergencia", "Competencia de Precios"
    event_description: str


# --- IMPLEMENTACIÓN DE APIS ---

# API 1: GET /geo/context
@app.get("/geo/context", response_model=Dict[str, str])
def get_geo_context():
    """Simula la respuesta de Geo-IP."""
    return {"region": "Lima", "age_stage": "Brote"}


# API 2: GET /kiosco/products/{region}
@app.get("/kiosco/products/{region}", response_model=List[Dict[str, Any]])
def get_products(region: str):
    """Devuelve los datos de productos de la región cargados desde products.json."""
    if region not in PRODUCTS_DATA:
        raise HTTPException(status_code=404, detail=f"Región '{region}' no encontrada.")
    return PRODUCTS_DATA[region]


# API 3: POST /kiosco/transaccion
@app.post("/kiosco/transaccion", response_model=KioscoState)
def process_transaction(transaction: TransactionRequest):
    current_state = transaction.user_state
    
    product_price = None
    for region_products in PRODUCTS_DATA.values():
        for product in region_products:
            if product["name"] == transaction.product_name:
                product_price = product["price"]
                break
        if product_price:
            break

    if not product_price:
        raise HTTPException(status_code=400, detail="Producto no válido.")

    total_cost = product_price * transaction.quantity
    
    if transaction.is_sale:
        if current_state.inventario.get(transaction.product_name, 0) < transaction.quantity:
             raise HTTPException(status_code=400, detail="Venta fallida: Inventario insuficiente.")
             
        current_state.saldo_actual += total_cost
        current_state.inventario[transaction.product_name] -= transaction.quantity
             
    else:
        if current_state.saldo_actual < total_cost:
            raise HTTPException(status_code=400, detail="Saldo insuficiente para la compra.")
        
        current_state.saldo_actual -= total_cost
        current_state.inventario[transaction.product_name] = current_state.inventario.get(transaction.product_name, 0) + transaction.quantity

    return current_state


# API 4: POST /ia/chat
@app.post("/ia/chat", response_model=ChatMessage)
def chat_with_yachaq(request: ChatRequest):
    """Simula una conversación con el chatbot YACHAQ, usando el contexto del kiosco."""
    
    # 1. INTEGRACIÓN DEL SYSTEM PROMPT (P2)
    # Se simula la creación del prompt final inyectando las variables de contexto.
    final_system_prompt = SYSTEM_PROMPT_TEMPLATE.format(
        region=request.region,
        age_stage=request.age_stage
    )
    # En un entorno real, este prompt se enviaría a Gemini/GPT junto con new_message.
    
    # 2. LÓGICA DE RESPUESTA SIMULADA (contextualizada)
    user_msg = request.new_message.lower()
    
    if "saldo" in user_msg or "dinero" in user_msg:
        response = f"Tu saldo actual es de S/ {request.user_context.saldo_actual:.2f}. Recuerda que estamos en la región de **{request.region}**, y cada centavo cuenta. ¡Siempre piensa en tu próximo movimiento!"
    elif "inventario" in user_msg or "productos" in user_msg:
        response = f"Tienes {sum(request.user_context.inventario.values())} artículos. Si estás en la etapa '{request.age_stage}', enfócate en los productos esenciales. ¡Revisa qué se vende más en **{request.region}**!"
    elif "reto" in user_msg or "evento" in user_msg:
        response = "El Reto del Sol te enseña sobre riesgos y oportunidades inesperadas, ¡algo clave para un 'emprendedor' en **{request.region}**! Analiza bien tus opciones antes de actuar."
    else:
        response = "Soy YACHAQ. ¿Qué pregunta tienes sobre tu kiosco o tus finanzas? Si tienes dudas sobre tu región, ¡dímelo!"
        
    return {"role": "assistant", "content": response}


# API 5: POST /ia/feedback
@app.post("/ia/feedback", response_model=ChatMessage)
def provide_pedagogical_feedback(request: FeedbackRequest):
    """Genera un comentario pedagógico simulado basado en el resultado de una transacción o evento."""
    
    # Se simula la inyección del contexto pedagógico para guiar la respuesta.
    # El prompt final no se usa completamente, solo la lógica.
    
    focus = request.pedagogical_focus
    result = request.financial_result
    
    if result >= 0:
        # Ganancia o Gasto controlado
        if "Fondo de emergencia" in focus:
            response = f"¡Excelente! Viste el evento '{request.event_description}'. Superaste el reto relacionado con el '{focus}'. Tener un fondo de emergencia te ayudó a manejar el gasto sin problemas en tu kiosco de **{request.region}**."
        elif "Competencia de Precios" in focus:
             response = f"¡Has gestionado la competencia de precios de **{request.region}** con éxito! Mantener la calidad o tu buena ubicación te hizo ganar."
        else:
            response = f"¡Tu decisión sobre '{focus}' fue muy rentable! Esto demuestra que sabes aprovechar las oportunidades en la etapa '{request.age_stage}'."
    else:
        # Pérdida o Gasto
        if "Riesgo y seguro" in focus:
            response = f"El evento '{request.event_description}' te afectó (Riesgo). Perdiste S/ {abs(result):.2f}. En el futuro, piensa en cómo puedes protegerte de este tipo de eventos, como con un seguro ficticio."
        elif "Competencia de Precios" in focus:
            response = f"Perdiste S/ {abs(result):.2f} debido a la competencia. En la región de **{request.region}**, siempre debes estar atento a lo que hacen tus vecinos. Es una lección importante sobre la competencia."
        else:
            response = f"Es una lección importante. Perdiste S/ {abs(result):.2f} debido al evento '{focus}'. Es parte del riesgo de manejar un negocio. ¡No te rindas!"
            
    return {"role": "assistant", "content": response}


# API 6: GET /reto/event
@app.get("/reto/event", response_model=Dict[str, Any])
def get_reto_event():
    """Genera un evento aleatorio para el Reto del Sol."""
    if not RETO_EVENTS:
        raise HTTPException(status_code=500, detail="No hay eventos definidos para el Reto del Sol.")
        
    return random.choice(RETO_EVENTS)