"""
PERSONAL DATA VALIDATOR API - PROJECT COMPLETE

Date: 11 December 2025
Status: 100% Functional and Production-Ready
Stack: FastAPI + Pydantic + Python 3.12
Tests: 11/11 ✓ (All passing)

PROJECT STRUCTURE
-----------------

API_Validadora/
   - main.py                    → Main FastAPI application
      • 3 endpoints: GET /, GET /health, POST /validate
      • Request logging
      • Global error handling
      • Auto-generated Swagger UI

   - app/                       → Modular package
      • models.py                 → Pydantic models (main model: UsuarioValidation)
      • validators.py             → Custom validation helpers

   - test_api.py                → 11 automated test cases
   - requirements.txt           → Project dependencies
   - README.md                  → Full documentation (install, usage, examples)
   - EJEMPLOS.md                → Usage examples (cURL, Python, JS)
   - .env.example               → Example environment variables

FEATURES
--------

Endpoints:
   • GET /        → API info
   • GET /health  → Health check
   • POST /validate → Validate personal data

Validations:
   • First name: min 2 chars, auto-normalized
   • Last name: min 2 chars, auto-normalized
   • Email: validated with email-validator
   • Phone: numeric, min 7 digits (optional)
   • Age: integer, range 0-120 (optional)

How to use
----------

1) Start the API
    $ cd /home/pantuflitos/Proyectos/API_Validadora
    $ python -m uvicorn main:app --host localhost --port 8000

2) Access docs
    • Swagger UI: http://localhost:8000/docs
    • ReDoc: http://localhost:8000/redoc

3) Example request (cURL)
    $ curl -X POST http://localhost:8000/validate \
       -H "Content-Type: application/json" \
       -d '{"first_name":"juan","last_name":"perez","email":"juan@example.com"}'

4) Run tests
    $ python test_api.py

Example responses
-----------------

Successful validation (200):
{
   "valid": true,
   "message": "Data validated successfully",
   "data": {
      "first_name": "Juan",
      "last_name": "Perez",
      "email": "juan.perez@example.com",
      "phone": "1234567890",
      "age": 30
   },
   "timestamp": "2025-12-11T22:50:31.141245"
}

Validation error (422):
{
   "detail": [
      {
         "type": "value_error",
         "loc": ["body", "first_name"],
         "msg": "Value error, Must have at least 2 characters",
         "input": "a"
      }
   ]
}

Dependencies
------------

fastapi==0.104.1
pydantic==2.5.0
pydantic-extra-types==2.1.0
uvicorn[standard]==0.24.0
email-validator==2.1.0
python-multipart==0.0.6
requests

Tests
-----

✓ Root endpoint
✓ Health check
✓ Successful validation
✓ Validation without optional fields
✓ First name too short
✓ Invalid email
✓ Phone too short
✓ Phone not numeric
✓ Age out of range
✓ Missing required fields
✓ Name normalization

All tests passing: 11/11 ✓

Notes
-----

The project is modular, well-documented, and ready for extension:
- Add a database (SQLAlchemy)
- Implement auth (JWT)
- Add caching, rate limiting, CI/CD, Docker support

"""

if __name__ == "__main__":
      print(__doc__)
