from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.database import engine, Base
from app.routes.todos import router as todos_router

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI application
app = FastAPI(
    title="Todo API",
    description="A simple Todo API built with FastAPI and SQLite",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(todos_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to Todo API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}