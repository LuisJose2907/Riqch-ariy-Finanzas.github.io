#!/bin/bash

# Este script se ejecuta al inicio del contenedor.

# 1. (Opcional) Instala dependencias nuevamente (Azure ya lo hace, pero esto puede ayudar)
pip install -r requirements.txt

# 2. Comando para iniciar la aplicación Uvicorn/FastAPI con Gunicorn
# Asegúrate de usar el formato correcto (main:app, servicio:api, etc.)
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app