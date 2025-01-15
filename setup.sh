#!/bin/bash
echo "Configurando el frontend..."
cd frontend
npm install

echo "Configurando el backend..."
cd ../backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "¡Configuración completada!"
