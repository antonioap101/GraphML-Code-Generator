# GraphML Code Generator

![GraphML Logo](https://via.placeholder.com/800x200.png?text=GraphML+Code+Generator)

## 🌐 Aplicación Deployada
Puedes acceder a la aplicación deployada en Vercel a través del siguiente enlace:  
[GraphML Code Generator en Vercel](https://graph-ml-code-generator-aag.vercel.app/)

---

## 📖 Descripción

**GraphML Code Generator** es una aplicación diseñada para convertir contenido XML en GraphML de manera eficiente y rápida. La herramienta está compuesta por un frontend desarrollado en `Vite + React` y un backend construido con `Python (FastAPI)`.  

Con esta aplicación, puedes cargar tus archivos XML y obtener su representación en formato GraphML, ampliamente utilizado en proyectos de grafos y visualización de datos.

---

## 🎯 Características

- **Conversión XML a GraphML:** Transforma archivos XML en GraphML de forma directa.
- **Interfaz de Usuario Moderna:** Una interfaz intuitiva y amigable para los usuarios.
- **Desempeño Altamente Optimizado:** Gracias a Vite y FastAPI, la experiencia es rápida y fluida.
- **Backend Escalable:** Ideal para integraciones con otros sistemas.
- **Fácil de Usar:** Diseñada para simplificar la conversión.

---

## 🚀 Tecnologías Utilizadas

- **Frontend:** 
  - Vite
  - React
  - TypeScript
- **Backend:** 
  - FastAPI
  - Python
  - Uvicorn
- **Hosting:** 
  - Vercel

---

## 📸 Imágenes

### Vista Principal
![Vista Principal](https://via.placeholder.com/800x400.png?text=Vista+Principal)

### Ejemplo de Conversión
![Ejemplo de Conversión](https://via.placeholder.com/800x400.png?text=Ejemplo+de+Conversión)

---

## 🔧 Configuración Local

Si deseas ejecutar el proyecto localmente, sigue los siguientes pasos:

### Requisitos Previos
- Node.js v16 o superior
- Python 3.9 o superior
- Vite y npm instalados

### Pasos para Ejecutar

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu_usuario/graphml-code-generator.git
   cd graphml-code-generator
   ```

2. **Configuración del Frontend**:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

3. **Configuración del Backend**:
   ```bash
   cd ../api
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   uvicorn app:app --reload
   ```

4. Abre la aplicación en tu navegador:
   - Frontend: [http://localhost:5173](http://localhost:5173)
   - Backend: [http://localhost:8000](http://localhost:8000)

---

## 🛠️ Desarrollo y Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de abrir un **Pull Request** o reportar problemas en la sección de [Issues](https://github.com/antonioap101/GraphML-Code-Generator/issues).

---

## 📝 Licencia

Este proyecto está bajo la licencia **MIT**. Puedes consultar más detalles en el archivo `LICENSE`.

---

## 🌟 ¡Gracias por tu interés en este proyecto!

Si te resulta útil, no dudes en dejar una estrella ⭐ en el repositorio. 😊
