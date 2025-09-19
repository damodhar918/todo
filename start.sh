#!/bin/bash

# Start backend server
echo "Starting FastAPI backend..."
cd backend
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# Install dependencies
pip install -r requirements.txt

# Start backend server in background
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 &

echo "Backend started on http://localhost:8000"
echo "API documentation available at http://localhost:8000/docs"

# Start frontend
echo "Starting Next.js frontend..."
cd ../frontend

# Install dependencies
npm install

# Start frontend server
echo "Frontend starting on http://localhost:3000"
npm run dev