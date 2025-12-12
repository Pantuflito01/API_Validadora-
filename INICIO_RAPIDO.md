# 🚀 Quick Start Guide

## ⚡ 30 seconds to get the API running

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Start the server
```bash
python -m uvicorn main:app --host localhost --port 8000
```

### 3️⃣ Open interactive docs
```
http://localhost:8000/docs
```

---

## 📝 Try the API

### Using curl (terminal)

**Successful validation:**
```bash
curl -X POST "http://localhost:8000/validate" \
  -H "Content-Type: application/json" \
  -d '{"first_name":"juan","last_name":"perez","email":"juan@example.com"}'
```

**Response:**
```json
{
  "valid": true,
  "message": "Data validated successfully",
  "data": {
    "first_name": "Juan",
    "last_name": "Perez",
    "email": "juan@example.com",
    "phone": null,
    "age": null
  }
}
```

### Using Python

```python
import requests

url = "http://localhost:8000/validate"
payload = {
    "first_name": "maria",
    "last_name": "garcia",
    "email": "maria@example.com",
    "phone": "1234567",
    "age": 28
}

response = requests.post(url, json=payload)
print(response.json())
```

### Using JavaScript/Fetch

```javascript
const payload = {
  first_name: "carlos",
  last_name: "lopez",
  email: "carlos@example.com"
};

fetch('http://localhost:8000/validate', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(payload)
})
.then(r => r.json())
.then(data => console.log(data));
```

---

## 🧪 Run tests

```bash
python test_api.py
```

Expected result: **11/11 tests passing ✓**

---

## 📚 Documentation

| Link | Description |
|------|------------|
| [README.md](README.md) | Full documentation |
| [EJEMPLOS.md](EJEMPLOS.md) | Examples in multiple languages |
| http://localhost:8000/docs | Swagger UI interactive |
| http://localhost:8000/redoc | ReDoc documentation |

---

## 🎯 Validation fields

| Field | Required | Validation |
|-------|----------|-----------|
| **first_name** | ✅ Yes | Minimum 2 characters |
| **last_name** | ✅ Yes | Minimum 2 characters |
| **email** | ✅ Yes | Must be a valid email format |
| **phone** | ❌ No | Digits only, minimum 7 |
| **age** | ❌ No | Between 0 and 120 |

---

## 🚨 Common errors

### Error: "Connection refused"
- Make sure the server is running: `python -m uvicorn main:app --host localhost --port 8000`

### Error: "Module not found"
- Install dependencies: `pip install -r requirements.txt`

### Error: "Invalid email"
- Verify the email format: `user@domain.com`

---

## 🎉 Ready!

Your REST API is fully functional and ready to:
- ✅ Test locally
- ✅ Integrate with your application
- ✅ Deploy to production
- ✅ Scale as needed

Have fun building! 🚀
