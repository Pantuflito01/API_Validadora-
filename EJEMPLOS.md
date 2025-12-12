# Examples for the Personal Data Validator API

## cURL examples

### 1) Health check
```bash
curl http://localhost:8000/health
```

### 2) API info
```bash
curl http://localhost:8000/
```

### 3) Successful validation (all fields)
```bash
curl -X POST http://localhost:8000/validate \
    -H "Content-Type: application/json" \
    -d '{
        "first_name": "juan",
        "last_name": "perez",
        "email": "juan.perez@example.com",
        "phone": "1234567890",
        "age": 30
    }'
```

### 4) Validation with required fields only
```bash
curl -X POST http://localhost:8000/validate \
    -H "Content-Type: application/json" \
    -d '{
        "first_name": "maria",
        "last_name": "garcia",
        "email": "maria.garcia@example.com"
    }'
```

### 5) Invalid email example
```bash
curl -X POST http://localhost:8000/validate \
    -H "Content-Type: application/json" \
    -d '{
        "first_name": "carlos",
        "last_name": "lopez",
        "email": "invalid-email"
    }'
```

### 6) Save response to file
```bash
curl -X POST http://localhost:8000/validate \
    -H "Content-Type: application/json" \
    -d '{
        "first_name": "ana",
        "last_name": "martinez",
        "email": "ana@example.com"
    }' > response.json
```

### 7) Pretty-print JSON
```bash
curl -X POST http://localhost:8000/validate \
    -H "Content-Type: application/json" \
    -d '{
        "first_name": "luis",
        "last_name": "rodriguez",
        "email": "luis@example.com",
        "age": 25
    }' | python -m json.tool
```

## Python (requests)

### Basic usage
```python
import requests

url = "http://localhost:8000/validate"
payload = {
        "first_name": "juan",
        "last_name": "perez",
        "email": "juan.perez@example.com",
        "phone": "1234567890",
        "age": 30
}

response = requests.post(url, json=payload)
print(response.json())
```

### Handling errors
```python
import requests

url = "http://localhost:8000/validate"
payload = {
        "first_name": "a",  # Too short
        "last_name": "perez",
        "email": "juan.perez@example.com"
}

response = requests.post(url, json=payload)
if response.status_code == 200:
        print("✓ OK", response.json())
elif response.status_code == 422:
        print("✗ Validation error", response.json())
else:
        print(f"✗ Server error: {response.status_code}")
```

### Validate multiple users
```python
import requests

users = [
        {
                "first_name": "juan",
                "last_name": "perez",
                "email": "juan@example.com",
                "phone": "1234567890",
                "age": 30
        },
        {
                "first_name": "maria",
                "last_name": "garcia",
                "email": "maria@example.com",
                "age": 25
        }
]

url = "http://localhost:8000/validate"
for user in users:
        resp = requests.post(url, json=user)
        if resp.status_code == 200:
                data = resp.json()["data"]
                print(f"✓ {data['first_name']} {data['last_name']} - {data['email']}")
        else:
                print(f"✗ Error validating: {user}")
```

## httpx (async)

```python
import httpx
import asyncio
import json

async def validate_user():
        async with httpx.AsyncClient() as client:
                payload = {
                        "first_name": "juan",
                        "last_name": "perez",
                        "email": "juan@example.com"
                }
                resp = await client.post("http://localhost:8000/validate", json=payload)
                print(json.dumps(resp.json(), indent=2))

asyncio.run(validate_user())
```

## Testing (pytest)

Run the included test script:

```bash
python test_api.py
```
            "email": "juan@example.com"

def test_validacion_exitosa():
    """Prueba que una validación exitosa devuelve 200"""
    respuesta = client.post(
        "/validar",
        json={
            "nombre": "juan",
            "apellido": "perez",
            "email": "juan@example.com"
        }
    )
    assert respuesta.status_code == 200
    assert respuesta.json()["valido"] == True

def test_email_invalido():
    """Prueba que un email inválido devuelve 422"""
    respuesta = client.post(
        "/validar",
        json={
            "nombre": "juan",
            "apellido": "perez",
            "email": "email-invalido"
        }
    )
    assert respuesta.status_code == 422

def test_nombre_muy_corto():
    """Prueba que nombres cortos devuelven 422"""
    "first_name": "juan",
    "last_name": "perez",
    "email": "juan@example.com"
            "nombre": "a",
            "apellido": "perez",
            "email": "test@example.com"
        }
    )
    assert respuesta.status_code == 422

def test_normalizacion_nombres():
    """Prueba que los nombres se normalizan correctamente"""
    respuesta = client.post(
        "/validar",
        json={
            "nombre": "jUaN",
            "apellido": "pErEz",
            "email": "test@example.com"
        }
    )
    assert respuesta.status_code == 200
    datos = respuesta.json()["datos"]
    assert datos["nombre"] == "Juan"
    assert datos["apellido"] == "Perez"

# Ejecutar con: pytest
```
            "first_name": "juan",
            "last_name": "perez",
            "email": "juan@example.com"
## 📡 Ejemplo con JavaScript/Fetch

```javascript
// Validación exitosa
const validarUsuario = async () => {
  const datos = {
    nombre: "juan",
    apellido: "perez",
    email: "juan@example.com",
    telefono: "1234567890",
    edad: 30
  };

  try {
    const respuesta = await fetch("http://localhost:8000/validar", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(datos)
    });

    if (respuesta.ok) {
      const resultado = await respuesta.json();
      console.log("✓ Validación exitosa:", resultado);
    } else {
      const error = await respuesta.json();
      console.error("✗ Error de validación:", error);
    }
  } catch (error) {
    console.error("✗ Error de conexión:", error);
  }
};

// Ejecutar
validarUsuario();
```

---

## 🔄 Validar en batch (Python)

```python
import requests
import json
from concurrent.futures import ThreadPoolExecutor

def validar_usuario(usuario):
    """Valida un usuario y devuelve resultado"""
    try:
        respuesta = requests.post(
            "http://localhost:8000/validar",
            json=usuario,
            timeout=5
        )
        return {
            "usuario": usuario["email"],
            "valido": respuesta.status_code == 200,
            "respuesta": respuesta.json()
        }
    except Exception as e:
        return {
            "usuario": usuario["email"],
            "valido": False,
            "error": str(e)
        }

# Lista de usuarios a validar
usuarios = [
    {"nombre": "juan", "apellido": "perez", "email": "juan@example.com"},
    {"nombre": "maria", "apellido": "garcia", "email": "maria@example.com"},
    {"nombre": "carlos", "apellido": "lopez", "email": "carlos@example.com"},
]

# Validar en paralelo
with ThreadPoolExecutor(max_workers=3) as executor:
    resultados = list(executor.map(validar_usuario, usuarios))

# Mostrar resultados
for resultado in resultados:
    estado = "✓" if resultado["valido"] else "✗"
    print(f"{estado} {resultado['usuario']}")
```

---

Estos ejemplos cubren casos de uso comunes y pueden adaptarse según tus necesidades.
