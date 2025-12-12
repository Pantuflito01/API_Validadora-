# Useful Commands

## Basic operations

### Install dependencies
```bash
pip install -r requirements.txt
```

### Start the server
```bash
python -m uvicorn main:app --host localhost --port 8000
```

### Start in development mode (auto-reload)
```bash
python -m uvicorn main:app --host localhost --port 8000 --reload
```

### Run tests
```bash
python test_api.py
```

---

## cURL examples

### Health check
```bash
curl http://localhost:8000/health
```

### API info
```bash
curl http://localhost:8000/
```

### Successful validation (all fields)
```bash
curl -X POST "http://localhost:8000/validate" \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "juan",
    "last_name": "perez",
    "email": "juan@example.com",
    "phone": "1234567890",
    "age": 30
  }'
```

### Required fields only
```bash
curl -X POST "http://localhost:8000/validate" \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "maria",
    "last_name": "garcia",
    "email": "maria@example.com"
  }'
```

### Validation error (first name too short)
```bash
curl -X POST "http://localhost:8000/validate" \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "a",
    "last_name": "perez",
    "email": "test@example.com"
  }'
```

### Validation error (invalid email)
```bash
curl -X POST "http://localhost:8000/validate" \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "juan",
    "last_name": "perez",
    "email": "invalid-email"
  }'
```

### Validation error (phone too short)
```bash
curl -X POST "http://localhost:8000/validate" \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "juan",
    "last_name": "perez",
    "email": "juan@example.com",
    "phone": "123"
  }'
```

### Validation error (age out of range)
```bash
curl -X POST "http://localhost:8000/validate" \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "juan",
    "last_name": "perez",
    "email": "juan@example.com",
    "age": 150
  }'
```

---

## Python examples (requests)

### Simple test script
```python
import requests

url = "http://localhost:8000/validate"

# Valid data
payload = {
    "first_name": "carlos",
    "last_name": "lopez",
    "email": "carlos@example.com",
    "age": 25
}

response = requests.post(url, json=payload)
print(response.json())
```

### Helper function with validations
```python
import requests

def validate_user(first_name, last_name, email, phone=None, age=None):
    url = "http://localhost:8000/validate"
    payload = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }
    if phone:
        payload["phone"] = phone
    if age:
        payload["age"] = age

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("✅ Validation successful")
        print(response.json()["data"])
    else:
        print("❌ Validation error")
        print(response.json())

# Run
validate_user("juan", "perez", "juan@example.com", "1234567890", 30)
```

---

## JavaScript (fetch / axios)

### Fetch API
```javascript
const validate = async (first_name, last_name, email, phone, age) => {
  const payload = { first_name, last_name, email };
  if (phone) payload.phone = phone;
  if (age) payload.age = age;

  const response = await fetch('http://localhost:8000/validate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });

  const result = await response.json();
  console.log(result);
};

// Usage
validate('juan', 'perez', 'juan@example.com', '1234567890', 30);
```

### Axios
```javascript
const axios = require('axios');

axios.post('http://localhost:8000/validate', {
  first_name: 'juan',
  last_name: 'perez',
  email: 'juan@example.com',
  phone: '1234567890',
  age: 30
})
.then(res => console.log(res.data))
.catch(err => console.log(err.response.data));
```

---

## 📊 Otras Herramientas

### Con wget
```bash
wget --post-data='{"nombre":"juan","apellido":"perez","email":"juan@example.com"}' \
     --header='Content-Type: application/json' \
     http://localhost:8000/validar -O -
```

### Con Postman
1. Nuevo Request → POST
2. URL: `http://localhost:8000/validar`
3. Headers: `Content-Type: application/json`
4. Body (raw JSON):
```json
{
  "nombre": "juan",
  "apellido": "perez",
  "email": "juan@example.com"
}
```
5. Click en "Send"

### Con httpie (más legible que curl)
```bash
http POST localhost:8000/validar \
  nombre=juan \
  apellido=perez \
  email=juan@example.com
```

---

## 🔍 Verificación y Debugging

### Ver logs del servidor
```bash
# El servidor muestra los logs en la terminal donde se ejecutó
# Busca líneas como:
# INFO:     Petición POST /validar - Email: ...
# INFO:     Validación exitosa para: ...
```

### Verificar que el servidor está activo
```bash
curl -I http://localhost:8000/health
```

### Ver todos los procesos Python
```bash
ps aux | grep python
```

### Detener el servidor
```bash
# En la terminal donde corre el servidor:
# Presiona Ctrl+C
```

---

## 📈 Monitoreo

### Contar peticiones exitosas
```bash
# Ver los logs del servidor y contar líneas con "Validación exitosa"
# En tiempo real:
tail -f logs.txt | grep "Validación exitosa"
```

### Ver estadísticas de peticiones
```bash
# En los logs buscar:
grep "Petición POST" server_logs.txt | wc -l
```

---

## 🚨 Troubleshooting

### Error: "Connection refused"
```bash
# El servidor no está corriendo
# Solución: Inicia el servidor
python -m uvicorn main:app --host localhost --port 8000
```

### Error: "ModuleNotFoundError"
```bash
# Las dependencias no están instaladas
# Solución:
pip install -r requirements.txt
```

### Error: "Port 8000 already in use"
```bash
# Otro proceso está usando el puerto
# Solución 1: Usa otro puerto
python -m uvicorn main:app --host localhost --port 8001

# Solución 2: Detén el proceso anterior
# Busca el PID y detén: kill -9 <PID>
```

---

## 💡 Tips Útiles

### Guardar respuestas en archivo
```bash
curl -X POST "http://localhost:8000/validar" \
  -H "Content-Type: application/json" \
  -d '{...}' > respuesta.json
```

### Probar múltiples usuarios
```bash
for i in {1..5}; do
  curl -X POST "http://localhost:8000/validar" \
    -H "Content-Type: application/json" \
    -d "{\"nombre\":\"usuario$i\",\"apellido\":\"test\",\"email\":\"user$i@example.com\"}"
  echo ""
done
```

### Medir tiempo de respuesta
```bash
curl -w "\nTiempo: %{time_total}s\n" http://localhost:8000/health
```

---

¡Estos comandos te ayudarán a probar y verificar la API completamente! 🚀
