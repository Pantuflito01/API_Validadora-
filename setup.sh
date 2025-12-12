#!/bin/bash

# Quick start script for the Personal Data Validator API

echo "============================================================"
echo "🚀 Personal Data Validator API - Quick Start"
echo "============================================================"
echo ""

# Check Python
if ! command -v python &> /dev/null; then
    echo "❌ Python is not installed"
    exit 1
fi

echo "✓ Python found: $(python --version)"
echo ""

# Create virtual environment if missing
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install -q -r requirements.txt

echo ""
echo "============================================================"
echo "✅ Setup complete"
echo "============================================================"
echo ""
echo "Available actions:"
echo ""
echo "1) Start server:      python -m uvicorn main:app --host localhost --port 8000"
echo "2) Run tests:         python test_api.py"
echo "3) Open Swagger UI:   http://localhost:8000/docs"
echo ""
echo "============================================================"
