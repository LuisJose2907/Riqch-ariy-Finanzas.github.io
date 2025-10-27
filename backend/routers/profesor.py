# backend/routers/profesor.py

from pydantic import BaseModel
from typing import List
from fastapi import APIRouter, HTTPException # Importamos HTTPException para errores

# --- MODELO DE SALIDA (Ya existente - Tarea 4) ---
class StudentProgress(BaseModel):
    id: int
    name: str
    level: str
    rentability: float
    
    class Config:
        from_attributes = True

# --- NUEVO MODELO DE ENTRADA (Para la Tarea 5) ---
class AdjustmentRequest(BaseModel):
    # Campos que el frontend envía en el POST
    student_id: int
    adjustment_type: str # Debe ser 'increase' o 'reinforce'

router = APIRouter(
    prefix="/profesor",
    tags=["Profesor Dashboard"],
    # Aquí se añadiría la seguridad con Depends(get_current_active_user)
)

# --- API 4: Obtener Progreso (Simulación) ---
@router.get("/progreso_clase", response_model=List[StudentProgress])
def get_progreso_clase():
    # Simulación de que la BD devuelve los datos necesarios
    return [
        {"id": 1, "name": "Juan Pérez", "level": "Etapa Brote", "rentability": 0.85},
        {"id": 2, "name": "María López", "level": "Etapa Brote", "rentability": 0.72},
        {"id": 3, "name": "Carlos Díaz", "level": "Etapa Madurez", "rentability": 0.55},
    ]

# --- API 5: Ajustar Nivel (Implementación de la Lógica) ---
@router.post("/ajustar_nivel")
def adjust_student_level(request: AdjustmentRequest): # Usa el modelo Pydantic de entrada
    
    student_id = request.student_id
    adjustment_type = request.adjustment_type
    
    # 1. Validación de Comando
    if adjustment_type not in ["increase", "reinforce"]:
        raise HTTPException(status_code=400, detail="Tipo de ajuste no válido.")

    # 2. Lógica de Modificación de Base de Datos (Simulación)
    try:
        if adjustment_type == 'increase':
            # **Aquí iría la llamada a la BD para aumentar la dificultad del juego**
            print(f"✅ BD: Dificultad AUMENTADA para estudiante ID: {student_id}")
            action_message = "Dificultad de la simulación ajustada a nivel superior (MARS)."
        elif adjustment_type == 'reinforce':
            # **Aquí iría la llamada a la BD para asignar un módulo de refuerzo**
            print(f"✅ BD: Módulo de REFUERZO ASIGNADO para estudiante ID: {student_id}")
            action_message = "Módulo de refuerzo académico/financiero asignado (MARS)."
            
        # 3. Retorno de Éxito
        return {
            "message": action_message, 
            "student_id": student_id,
            "status": "success"
        }
    except Exception as e:
        # 4. Manejo de Error de BD
        raise HTTPException(status_code=500, detail=f"Error al actualizar BD: {e}")