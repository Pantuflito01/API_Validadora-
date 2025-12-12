#!/bin/bash

# QUICK START - Personal Data Validator API
# ========================================

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║          PERSONAL DATA VALIDATOR - QUICK START INSTRUCTIONS     ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

echo "Project directory:"
echo "   /home/pantuflitos/Proyectos/API_Validadora"
echo ""

echo "STEP 1: Change to project directory"
echo "   cd /home/pantuflitos/Proyectos/API_Validadora"
echo ""

echo "STEP 2: Activate virtual environment (if needed)"
echo "   source .venv/bin/activate"
echo ""

echo "STEP 3: Start the API"
echo "   python -m uvicorn main:app --host localhost --port 8000"
echo ""

echo "STEP 4: Access the API"
echo "   Swagger UI: http://localhost:8000/docs"
echo "   ReDoc: http://localhost:8000/redoc"
echo "   Health: http://localhost:8000/health"
echo ""

echo "Example request with cURL:"
echo '   curl -X POST http://localhost:8000/validate \'
echo '     -H "Content-Type: application/json" \'
echo '     -d '\''{
echo '       "first_name": "juan",
echo '       "last_name": "perez",
echo '       "email": "juan@example.com"
echo '     }'\'''
echo ""

echo "Run tests (in another terminal):"
echo "   python test_api.py"
echo ""

echo "════════════════════════════════════════════════════════════════"
echo ""
echo "Full documentation: README.md"
echo "More examples: EJEMPLOS.md"
echo ""
echo "✅ The API is ready to use."
echo ""
