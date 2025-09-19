@echo off

echo Starting FastAPI backend...
cd backend

if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

:: Activate virtual environment
call venv\Scripts\activate

:: Install dependencies
pip install -r requirements.txt

:: Start backend server in background
echo Backend starting on http://localhost:8000
echo API documentation available at http://localhost:8000/docs
start /B uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

:: Start frontend
echo Starting Next.js frontend...
cd ..\frontend

:: Install dependencies
npm install

:: Start frontend server
echo Frontend starting on http://localhost:3000
npm run dev