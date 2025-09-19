# Todo Application

A full-stack todo application built with **FastAPI** (Python) for the backend, **Next.js** (TypeScript) for the frontend, and **SQLite** as the database.

## 🚀 Features

- ✅ Create, read, update, and delete todos
- ✅ Mark todos as completed/pending
- ✅ Edit todo titles and descriptions
- ✅ Responsive web interface
- ✅ RESTful API with automatic documentation
- ✅ SQLite database with SQLAlchemy ORM
- ✅ CORS enabled for frontend-backend communication
- ✅ TypeScript support for type safety

## 🏗️ Project Structure

```
todo/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py         # Main FastAPI application
│   │   ├── crud.py         # Database operations
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── todo.py     # SQLAlchemy models
│   │   │   └── schemas.py  # Pydantic schemas
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   └── todos.py    # Todo API routes
│   │   └── database/
│   │       ├── __init__.py
│   │       └── database.py # Database configuration
│   ├── requirements.txt    # Python dependencies
│   └── todos.db           # SQLite database (created automatically)
├── frontend/               # Next.js frontend
│   ├── app/
│   │   ├── globals.css    # Global styles
│   │   ├── layout.tsx     # Root layout
│   │   └── page.tsx       # Home page
│   ├── components/
│   │   ├── AddTodoForm.tsx
│   │   ├── TodoItem.tsx
│   │   └── TodoList.tsx
│   ├── lib/
│   │   └── api.ts         # API client
│   ├── package.json
│   ├── tailwind.config.js
│   ├── next.config.js
│   └── tsconfig.json
└── README.md              # This file
```

## 🛠️ Technology Stack

### Backend
- **FastAPI** - Modern, fast web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **SQLite** - Lightweight database
- **Pydantic** - Data validation using Python type annotations
- **Uvicorn** - ASGI server implementation

### Frontend
- **Next.js 14** - React framework with App Router
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first CSS framework
- **Axios** - HTTP client for API calls
- **React Hooks** - State management

## 📋 Prerequisites

- **Python 3.8+**
- **Node.js 18+**
- **npm or yarn**

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd todo
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the FastAPI server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The backend API will be available at: `http://localhost:8000`

### 3. Frontend Setup

Open a new terminal and:

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

The frontend application will be available at: `http://localhost:3000`

## 📚 API Documentation

### Base URL
```
http://localhost:8000/api
```

### Endpoints

#### Get All Todos
```http
GET /todos/
```

**Query Parameters:**
- `skip` (integer, optional): Number of records to skip (default: 0)
- `limit` (integer, optional): Maximum number of records to return (default: 100)

**Response:**
```json
[
  {
    "id": 1,
    "title": "Sample Todo",
    "description": "This is a sample todo",
    "completed": false,
    "created_at": "2023-12-01T10:00:00Z",
    "updated_at": null
  }
]
```

#### Get Single Todo
```http
GET /todos/{todo_id}
```

**Response:**
```json
{
  "id": 1,
  "title": "Sample Todo",
  "description": "This is a sample todo",
  "completed": false,
  "created_at": "2023-12-01T10:00:00Z",
  "updated_at": null
}
```

#### Create Todo
```http
POST /todos/
```

**Request Body:**
```json
{
  "title": "New Todo",
  "description": "Optional description",
  "completed": false
}
```

**Response:**
```json
{
  "id": 2,
  "title": "New Todo",
  "description": "Optional description",
  "completed": false,
  "created_at": "2023-12-01T10:30:00Z",
  "updated_at": null
}
```

#### Update Todo
```http
PUT /todos/{todo_id}
```

**Request Body:**
```json
{
  "title": "Updated Todo",
  "description": "Updated description",
  "completed": true
}
```

**Response:**
```json
{
  "id": 1,
  "title": "Updated Todo",
  "description": "Updated description",
  "completed": true,
  "created_at": "2023-12-01T10:00:00Z",
  "updated_at": "2023-12-01T11:00:00Z"
}
```

#### Delete Todo
```http
DELETE /todos/{todo_id}
```

**Response:** `204 No Content`

### Interactive API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🎨 Frontend Components

### `TodoList.tsx`
Main component that orchestrates the todo application:
- Fetches todos from API
- Manages application state
- Handles error states and loading

### `AddTodoForm.tsx`
Form component for creating new todos:
- Input validation
- Handles form submission
- Provides user feedback

### `TodoItem.tsx`
Individual todo item component:
- Display todo information
- Toggle completion status
- Edit todo inline
- Delete todos with confirmation

## 🔧 Configuration

### Backend Configuration

The backend uses the following configuration in `app/database/database.py`:

```python
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"
```

To use a different database (PostgreSQL, MySQL, etc.), update this URL and install the appropriate database driver.

### Frontend Configuration

The frontend is configured to proxy API requests to the backend in `next.config.js`:

```javascript
async rewrites() {
  return [
    {
      source: '/api/:path*',
      destination: 'http://localhost:8000/api/:path*',
    },
  ]
}
```

## 🧪 Testing the Application

### Backend Testing

1. Start the backend server
2. Visit `http://localhost:8000/docs` for interactive API testing
3. Use the Swagger UI to test all endpoints

### Frontend Testing

1. Start both backend and frontend servers
2. Visit `http://localhost:3000`
3. Test all functionality:
   - Add new todos
   - Mark todos as complete/incomplete
   - Edit existing todos
   - Delete todos

### Manual API Testing with curl

```bash
# Get all todos
curl -X GET "http://localhost:8000/api/todos/"

# Create a new todo
curl -X POST "http://localhost:8000/api/todos/" \
  -H "Content-Type: application/json" \
  -d '{"title": "Test Todo", "description": "Testing the API"}'

# Update a todo (replace {id} with actual todo ID)
curl -X PUT "http://localhost:8000/api/todos/{id}" \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'

# Delete a todo (replace {id} with actual todo ID)
curl -X DELETE "http://localhost:8000/api/todos/{id}"
```

## 🚀 Deployment

### Backend Deployment

1. **Using Uvicorn in production:**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

2. **Using Docker:**
```dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```pip install -r requirements.txt

### Frontend Deployment

1. **Build for production:**
```bash
npm run build
npm start
```

2. **Deploy to Vercel:**
```bash
npm install -g vercel
vercel
```

## 🔍 Troubleshooting

### Common Issues

1. **CORS Errors**: Ensure the backend CORS configuration includes your frontend URL
2. **Database Issues**: Check if the SQLite database file has proper permissions
3. **Port Conflicts**: Make sure ports 3000 and 8000 are not being used by other applications
4. **Module Import Errors**: Verify all dependencies are installed correctly

### Debugging

1. **Backend Logs**: Check the uvicorn server logs for API errors
2. **Frontend Console**: Open browser DevTools to see frontend errors
3. **Network Tab**: Monitor API requests and responses in browser DevTools

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- FastAPI for the excellent web framework
- Next.js team for the React framework
- SQLAlchemy for the ORM
- Tailwind CSS for the styling framework

---

**Happy coding! 🎉**