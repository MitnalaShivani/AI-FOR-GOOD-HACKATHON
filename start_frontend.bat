@echo off
echo ========================================
echo Starting Blood Warriors Frontend Server
echo ========================================
echo.

cd frontend

REM Check if node_modules exists
if not exist "node_modules" (
    echo ERROR: Node modules not found
    echo Please run setup_windows.bat first
    pause
    exit /b 1
)

REM Check if package.json exists
if not exist "package.json" (
    echo ERROR: Frontend source files not found
    echo Please ensure you're in the correct directory
    pause
    exit /b 1
)

echo Starting React development server...
echo Frontend will be available at: http://localhost:5174
echo.
echo Press Ctrl+C to stop the server
echo.

REM Start the React development server
npm run dev

pause

