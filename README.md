# Task Management Application

A comprehensive task management solution built with Flask and Bootstrap, designed to help users organize and track their tasks efficiently.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Local Development Setup](#local-development-setup)
  - [Docker Setup](#docker-setup)
- [Environment Configuration](#environment-configuration)
- [Running the Application](#running-the-application)
- [Database Setup](#database-setup)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)

## Features

### Task Management
- Create, read, update, and delete tasks
- Set task priorities and due dates
- Track task progress
- Categorize tasks
- Search and filter tasks

### User Management
- User registration and authentication
- Profile management
- Password reset functionality
- Role-based access control

### User Interface
- Responsive design using Bootstrap
- Interactive dashboard
- Progress tracking visualizations
- Mobile-friendly interface

## Technologies Used
- **Backend**: Flask, Python 3.x
- **Database**: MySQL, SQLAlchemy ORM
- **Authentication**: Flask-Bcrypt
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **API Serialization**: Flask-Marshmallow
- **Templates**: Jinja2
- **Container**: Docker

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.11 or higher
- pip (Python package manager)
- MySQL Server
- Git
- Docker (optional, for containerized deployment)

## Installation

### Local Development Setup

1. **Clone the Repository**
```bash
git clone https://github.com/Tmiseray/Task-Management-Application.git
cd Task-Management-Application
```

2. **Create and Activate Virtual Environment**
```bash
# Create virtual environment
python -m venv env

# Activate virtual environment
# For Mac/Linux:
source env/bin/activate
# For Windows:
env\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure Environment Variables**
```bash
# Create .env file from example
cp .env.example .env
# Edit .env with your configuration
```

### Docker Setup

1. **Install Docker**
```bash
# For Mac (using Homebrew)
brew install --cask docker

# Launch Docker Desktop from Applications folder
# Wait for Docker to start (whale icon in menu bar)
```

2. **Verify Docker Installation**
```bash
docker --version
```

3. **Build and Run with Docker**
```bash
# Build the Docker image
docker build -t task-management-app .

# Run the container
docker run -p 5000:5000 task-management-app
```

4. **Using Docker Compose (recommended)**
```bash
# Start both application and database
docker-compose up

# Run in detached mode
docker-compose up -d

# Stop services
docker-compose down
```

## Environment Configuration

Create a `.env` file in the project root with the following variables:
```env
FLASK_APP=app.py
FLASK_ENV=development
FLASK_DEBUG=1
MYSQL_HOST=localhost
MYSQL_USER=your_user
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=task_management
SECRET_KEY=your_secret_key
```

## Running the Application

### Local Development
```bash
# Run with Flask
flask run

# Or with Python
python app.py
```
The application will be available at `http://127.0.0.1:5000`

### Docker Environment
```bash
# Using Docker
docker run -p 5000:5000 task-management-app

# Using Docker Compose
docker-compose up
```
The application will be available at `http://localhost:5000`

## Database Setup

### Local MySQL Setup
1. Install MySQL Server
2. Create database and user:
```sql
CREATE DATABASE task_management;
CREATE USER 'taskapp'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON task_management.* TO 'taskapp'@'localhost';
FLUSH PRIVILEGES;
```

### Using Docker MySQL
The docker-compose.yml file handles database setup automatically.

## Project Structure
```
task-management-app/
├── app.py                  # Application entry point
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
├── .env                  # Environment variables
├── .gitignore           # Git ignore rules
├── static/              # Static files (CSS, JS, images)
├── templates/           # HTML templates
└── models/              # Database models
```

## API Endpoints

### Task Endpoints
- `GET /tasks` - List all tasks
- `POST /tasks` - Create new task
- `GET /tasks/<id>` - Get task details
- `PUT /tasks/<id>` - Update task
- `DELETE /tasks/<id>` - Delete task

### User Endpoints
- `POST /register` - Register new user
- `POST /login` - User login
- `GET /profile` - Get user profile
- `PUT /profile` - Update profile

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Troubleshooting

### Common Issues

1. **MySQL Connection Error**
   - Verify MySQL is running
   - Check connection credentials
   - Ensure database exists

2. **Docker Issues**
   - Ensure Docker Desktop is running
   - Check port conflicts
   - Verify environment variables

3. **Package Installation Issues**
   - Update pip: `pip install --upgrade pip`
   - Install build dependencies: `brew install mysql-connector-c`
   - Use virtual environment

### Getting Help
- Open an issue on GitHub
- Check existing issues for solutions
- Review the error logs

For more detailed information, visit the [GitHub repository](https://github.com/Tmiseray/Task-Management-Application).
