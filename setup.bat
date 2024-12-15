@echo off
echo Configurando el frontend...
cd frontend
npm install

echo Configurando el backend...
cd ../api
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
echo Configuración completada!
