# API Validadora

FastAPI REST API for validating personal data using Pydantic.

Features
- Validate and normalize `nombre` (first name) and `apellido` (last name)
- Validate `email` using a robust validator
- Optional `telefono` (digits only, min 7) and `edad` (0-120)
- Automatic name capitalization
- Swagger UI and ReDoc documentation
- Logging and global error handling

Quick Start
1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app locally:

```bash
uvicorn main:app --host localhost --port 8000
```

4. Open Swagger UI: http://localhost:8000/docs

Endpoints
- `GET /` — API information and metadata
- `GET /health` — Health check
- `POST /validar` — Validate personal data (JSON body)

Example Request

```bash
curl -X POST "http://localhost:8000/validar" \
  -H "Content-Type: application/json" \
  -d '{"nombre":"juan","apellido":"perez","email":"juan@example.com","telefono":"1234567","edad":30}'
```

Example Response

```json
{
  "valido": true,
  "mensaje": "Datos validados correctamente",
  "datos": {
    "nombre": "Juan",
    "apellido": "Perez",
    "email": "juan@example.com",
    "telefono": "1234567",
    "edad": 30
  },
  "timestamp": "2025-12-11T22:56:11.327998"
}
```

Testing

Run the automated test suite:

```bash
python test_api.py
```

License

This project is licensed under the MIT License — see the `LICENSE` file for details.

Contributing

Contributions are welcome. Open an issue or a pull request on GitHub.

## Personal Data Validator API

This repository contains a production-ready FastAPI application (Python 3.12) that validates and normalizes personal data fields using Pydantic models and field validators. The project includes automated tests, complete documentation, and examples.

## Features

- Robust validation with Pydantic
- Automatic normalization of first and last names (capitalization)
- Email validation using a dedicated validator
- Phone validation (digits only, minimum 7 characters)
- Age validation (integer between 0 and 120)
- Auto-generated Swagger UI and ReDoc documentation
- Centralized error handling and structured logging

## Requirements

- Python 3.11 or later
- pip

## Installation

1. Clone the repository and enter the project folder:

```bash
git clone https://github.com/Pantuflito01/API_Validadora-.git
cd API_Validadora
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the API

Start the application with Uvicorn:

```bash
uvicorn main:app --host localhost --port 8000
```

The API will be available at http://localhost:8000.

## API Documentation

Open the interactive API docs at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Endpoints

1) `GET /` — API information and metadata

Example response (200):

```json
{
  "nombre": "API Validadora",
  "version": "1.0.0",
  "descripcion": "Personal data validation REST API",
  "documentacion": "http://localhost:8000/docs",
  "timestamp": "2025-12-11T22:50:31.132924"
}
```

2) `GET /health` — Health check

Example response (200):

```json
{
  "status": "healthy",
  "timestamp": "2025-12-11T22:50:31.134761"
}
```

3) `POST /validar` — Validate personal data

Request schema (JSON):

- `nombre` (string, required): minimum 2 characters
- `apellido` (string, required): minimum 2 characters
- `email` (string, required): valid email format
- `telefono` (string, optional): digits only, minimum 7 digits
- `edad` (integer, optional): 0-120

Example request:

```bash
curl -X POST http://localhost:8000/validar \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "juan",
    "apellido": "perez",
    "email": "juan.perez@example.com",
    "telefono": "1234567",
    "edad": 30
  }'
```

Successful response (200):

```json
{
  "valido": true,
  "mensaje": "Datos validados correctamente",
  "datos": {
    "nombre": "Juan",
    "apellido": "Perez",
    "email": "juan.perez@example.com",
    "telefono": "1234567",
    "edad": 30
  },
  "timestamp": "2025-12-11T22:50:31.141245"
}
```

Validation error example (422):

```bash
curl -X POST http://localhost:8000/validar \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "a",
    "apellido": "perez",
    "email": "invalid-email"
  }'
```

The server will return a 422 response with details about the failing fields.

## Testing

Run the automated test suite:

```bash
python test_api.py
```

## License

This project is licensed under the MIT License — see the `LICENSE` file for details.

## Contributing

Contributions are welcome. Please open an issue or a pull request on GitHub.


**Respuesta con error (422):**

```json
{
  "detail": [
    {
      "type": "value_error",
      "loc": ["body", "nombre"],
      "msg": "Value error, Debe tener mínimo 2 caracteres",
      "input": "a"
    },
    {
      "type": "value_error",
      "loc": ["body", "email"],
      "msg": "value is not a valid email address: The email address is not valid. It must have exactly one @-sign.",
      "input": "email-inválido"
    }
  ]
}
```

---

## 🧪 Pruebas

### Ejecutar script de pruebas automatizadas

```bash
python test_api.py
```

Este script ejecuta 11 pruebas diferentes que incluyen:

✅ Endpoint raíz  
✅ Health check  
✅ Validación exitosa  
✅ Validación sin campos opcionales  
✅ Error: Nombre muy corto  
✅ Error: Email inválido  
✅ Error: Teléfono muy corto  
✅ Error: Teléfono no numérico  
✅ Error: Edad fuera de rango  
✅ Error: Campos obligatorios faltantes  
✅ Normalización de nombres  

**Salida esperada:**
```
============================================================
PRUEBAS DE LA API VALIDADORA
============================================================
✓ API disponible en http://localhost:8000
...
Pruebas exitosas: 11/11
============================================================

¡Todas las pruebas pasaron correctamente!
```

---

## 🧩 Estructura del Proyecto

```
API_Validadora/
├── main.py                 # Aplicación principal (FastAPI)
├── app/
│   ├── __init__.py        # Inicializador del paquete
│   ├── models.py          # Modelos Pydantic con validadores
│   └── validators.py      # Funciones de validación personalizadas
├── test_api.py            # Script de pruebas automatizadas
├── requirements.txt       # Dependencias del proyecto
└── README.md             # Este archivo
```

---

## 📦 Dependencias

| Paquete | Versión | Propósito |
|---------|---------|----------|
| `fastapi` | 0.104.1 | Framework web moderno |
| `pydantic` | 2.5.0 | Validación de datos |
| `pydantic-extra-types` | 2.1.0 | Tipos adicionales de Pydantic |
| `uvicorn[standard]` | 0.24.0 | Servidor ASGI |
| `email-validator` | 2.1.0 | Validación de emails |
| `python-multipart` | 0.0.6 | Parseo de multipart/form-data |
| `requests` | (en test_api.py) | Cliente HTTP para pruebas |

---

## 🔍 Swagger UI (Documentación Interactiva)

Accede a la documentación interactiva y prueba los endpoints en tiempo real:

**URL:** http://localhost:8000/docs

En Swagger UI puedes:
- Ver todos los endpoints disponibles
- Probar las peticiones en tiempo real
- Ver esquemas JSON automáticos
- Visualizar ejemplos de respuestas

---

## 📊 Validaciones Implementadas

### Nombres y Apellidos
- ✅ Mínimo 2 caracteres
- ✅ Se capitalizan automáticamente (primera letra mayúscula, resto minúsculas)
- ✅ Se eliminan espacios en blanco innecesarios

### Email
- ✅ Formato válido según RFC 5322
- ✅ Validación con librería `email-validator`
- ✅ Campo obligatorio

### Teléfono
- ✅ Solo dígitos (0-9)
- ✅ Mínimo 7 dígitos
- ✅ Opcional (puede ser null)
- ✅ Se eliminan espacios en blanco

### Edad
- ✅ Rango 0-120 años
- ✅ Tipo int (entero)
- ✅ Opcional (puede ser null)

---

## 📝 Logging

La API registra automáticamente:
- Hora exacta de cada petición
- Endpoint solicitado
- Datos del usuario validado
- Resultado de la validación
- Errores y excepciones

**Ejemplo de logs:**
```
2025-12-11 22:50:31 - main - INFO - API Validadora iniciada correctamente
2025-12-11 22:50:31 - main - INFO - Petición POST /validar - Email: juan.perez@example.com, Nombre: juan, Apellido: perez
2025-12-11 22:50:31 - main - INFO - Validación exitosa para: juan.perez@example.com
```

---

## 🚀 Ejemplo de Uso Completo

### 1. Iniciar la API
```bash
python -m uvicorn main:app --host localhost --port 8000
```

### 2. Hacer una petición desde otro terminal o usando Postman

```bash
curl -X POST http://localhost:8000/validar \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "carlos",
    "apellido": "martinez",
    "email": "carlos.martinez@gmail.com",
    "telefono": "1234567890",
    "edad": 25
  }' | python -m json.tool
```

### 3. Respuesta esperada

```json
{
  "valido": true,
  "mensaje": "Datos validados correctamente",
  "datos": {
    "nombre": "Carlos",
    "apellido": "Martinez",
    "email": "carlos.martinez@gmail.com",
    "telefono": "1234567890",
    "edad": 25
  },
  "timestamp": "2025-12-11T22:50:31.141245"
}
```

---

## 🛠️ Personalización

### Cambiar puerto
```bash
python -m uvicorn main:app --host localhost --port 9000
```

### Cambiar host
```bash
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

### Modo desarrollo con auto-reload
```bash
python -m uvicorn main:app --host localhost --port 8000 --reload
```

---

## 📈 Escalabilidad

Este proyecto está diseñado para ser escalable:

- ✅ Estructura modular con separación de concerns
- ✅ Validadores reutilizables
- ✅ Manejadores de errores globales
- ✅ Logging centralizado
- ✅ Fácil de añadir nuevos endpoints
- ✅ Compatible con bases de datos (SQLAlchemy, etc.)
- ✅ Compatible con autenticación (JWT, OAuth2, etc.)

---

## 🐛 Resolución de Problemas

### Error: "ModuleNotFoundError: No module named 'fastapi'"
**Solución:** Asegúrate de instalar las dependencias: `pip install -r requirements.txt`

### Error: "Address already in use: ('localhost', 8000)"
**Solución:** El puerto 8000 ya está en uso. Usa otro puerto:
```bash
python -m uvicorn main:app --host localhost --port 8001
```

### Las validaciones no funcionan
**Solución:** Verifica que estés enviando los datos en formato JSON con el header `Content-Type: application/json`

---

## 📜 Licencia

Proyecto libre para uso educativo y profesional.

---

## 👨‍💻 Autor

Proyecto de API REST con FastAPI - Diciembre 2025

---

## 📞 Soporte

Para problemas o preguntas, revisa:
1. La documentación en Swagger: http://localhost:8000/docs
2. Este README
3. Los comentarios en el código

---

## ✨ Checklist de Implementación

- ✅ API REST funcional con FastAPI
- ✅ Endpoints POST /validar, GET /, GET /health
- ✅ Validación con Pydantic
- ✅ Normalización de nombres
- ✅ Validación de email con regex
- ✅ Validación de teléfono (numérico, 7+ dígitos)
- ✅ Validación de edad (0-120)
- ✅ Campos obligatorios: nombre, apellido, email
- ✅ Campos opcionales: teléfono, edad
- ✅ Manejo global de errores
- ✅ Logging por cada petición
- ✅ Swagger UI automático
- ✅ Código modular y limpio
- ✅ requirements.txt completo
- ✅ Script de pruebas automatizadas (11/11 ✅)
- ✅ Servir en localhost:8000 con uvicorn
- ✅ 100% funcional y lista para producción

¡La API está lista para usar! 🎉
