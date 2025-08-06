@echo off
echo ========================================
echo Starting Blood Warriors Backend Server
echo ========================================
echo.

cd backend

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found
    echo Please run setup_windows.bat first
    pause
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Check if required files exist
if not exist "src\main.py" (
    echo ERROR: Backend source files not found
    echo Please ensure you're in the correct directory
    pause
    exit /b 1
)

echo Starting Flask backend server...
echo Backend will be available at: http://localhost:5000
echo API documentation: http://localhost:5000/api/gemini/status
echo.
echo Press Ctrl+C to stop the server
echo.

REM Start the Flask application
python src\main.py

pause

