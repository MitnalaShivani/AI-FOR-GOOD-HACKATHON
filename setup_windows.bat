@echo off
echo ========================================
echo Blood Warriors AI System - Windows Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.11+ from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Node.js is not installed or not in PATH
    echo Please install Node.js 20.x LTS from https://nodejs.org/
    pause
    exit /b 1
)

echo ✓ Python and Node.js are installed
echo.

REM Setup Backend
echo Setting up Backend...
cd backend

REM Create virtual environment
echo Creating Python virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)

REM Activate virtual environment and install dependencies
echo Installing Python dependencies...
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install Python dependencies
    pause
    exit /b 1
)

echo ✓ Backend setup complete
echo.

REM Setup Frontend
echo Setting up Frontend...
cd ..\frontend

REM Install Node.js dependencies
echo Installing Node.js dependencies...
npm install
if %errorlevel% neq 0 (
    echo ERROR: Failed to install Node.js dependencies
    pause
    exit /b 1
)

echo ✓ Frontend setup complete
echo.

REM Initialize Database
echo Initializing database...
cd ..\backend
REM No explicit database initialization needed here, as the app will create it on first run.
REM If you need to create tables, you would add SQLAlchemy db.create_all() here.

REM Generate sample data
echo Generating sample data...
python data\generate_synthetic_data.py
if %errorlevel% neq 0 (
    echo WARNING: Sample data generation failed, but continuing...
)

REM Train models
echo Training AI models (this may take a few minutes)...
python models\train_xgboost.py
python models\train_lstm.py
if %errorlevel% neq 0 (
    echo WARNING: Model training failed, but continuing...
)

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To start the application:
echo 1. Run start_backend.bat to start the backend server
echo 2. Run start_frontend.bat to start the frontend server
echo 3. Open http://localhost:5174 in your browser
echo.
echo For more information, see INSTALLATION.md
echo.
pause

