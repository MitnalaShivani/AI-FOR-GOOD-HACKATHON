# Windows Setup Guide - Blood Warriors AI System

## 🪟 Windows Installation Guide

This guide is specifically designed for Windows users to set up and run the Blood Warriors AI-Powered Blood Donation Management System.

## 📋 Prerequisites for Windows

### Required Software

1. **Python 3.11 or higher**
   - Download from: https://www.python.org/downloads/
   - ⚠️ **IMPORTANT**: During installation, check "Add Python to PATH"
   - Verify installation: Open Command Prompt and type `python --version`

2. **Node.js 20.x LTS**
   - Download from: https://nodejs.org/
   - Choose the LTS version (recommended for most users)
   - Verify installation: Open Command Prompt and type `node --version`

3. **Git for Windows**
   - Download from: https://git-scm.com/download/win
   - Use default installation settings
   - Verify installation: Open Command Prompt and type `git --version`

### System Requirements

- **Windows 10** or **Windows 11**
- **8GB RAM** minimum (16GB recommended)
- **10GB free disk space**
- **Internet connection** for downloading dependencies

## 🚀 Quick Start (Automated Setup)

### Step 1: Download the Project

**Option A: Download ZIP file**
1. Download the `blood_donation_system_complete.zip` file
2. Extract it to a folder like `C:\blood_donation_system`
3. Open Command Prompt as Administrator
4. Navigate to the project folder:
   ```cmd
   cd C:\blood_donation_system
   ```

**Option B: Clone with Git**
```cmd
git clone https://github.com/blood-warriors/ai-donation-system.git
cd ai-donation-system
```

### Step 2: Run Automated Setup

```cmd
setup_windows.bat
```

This script will:
- ✅ Check if Python and Node.js are installed
- ✅ Create Python virtual environment
- ✅ Install all Python dependencies
- ✅ Install all Node.js dependencies
- ✅ Initialize the database
- ✅ Generate sample data
- ✅ Train AI models

### Step 3: Start the Application

**Start Backend (Terminal 1):**
```cmd
start_backend.bat
```

**Start Frontend (Terminal 2):**
```cmd
start_frontend.bat
```

### Step 4: Access the Application

- **Frontend**: http://localhost:5174
- **Backend API**: http://localhost:5000
- **API Status**: http://localhost:5000/api/gemini/status

## 🔧 Manual Setup (If Automated Setup Fails)

### Backend Setup

1. **Open Command Prompt as Administrator**

2. **Navigate to backend folder:**
   ```cmd
   cd blood_donation_system\backend
   ```

3. **Create virtual environment:**
   ```cmd
   python -m venv venv
   ```

4. **Activate virtual environment:**
   ```cmd
   venv\Scripts\activate
   ```

5. **Install dependencies:**
   ```cmd
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

6. **Initialize database:**
   ```cmd
   python -c "from src.main import app, db; app.app_context().push(); db.create_all(); print('Database initialized!')"
   ```

7. **Generate sample data:**
   ```cmd
   python data\generate_synthetic_data.py
   ```

8. **Train models:**
   ```cmd
   python models\train_xgboost.py
   python models\train_lstm.py
   ```

### Frontend Setup

1. **Open new Command Prompt**

2. **Navigate to frontend folder:**
   ```cmd
   cd blood_donation_system\frontend
   ```

3. **Install dependencies:**
   ```cmd
   npm install
   ```

### Starting the Application

1. **Start Backend (Command Prompt 1):**
   ```cmd
   cd blood_donation_system\backend
   venv\Scripts\activate
   python src\main.py
   ```

2. **Start Frontend (Command Prompt 2):**
   ```cmd
   cd blood_donation_system\frontend
   npm run dev
   ```

## 🐛 Windows-Specific Troubleshooting

### Common Issues and Solutions

**1. "Python is not recognized as an internal or external command"**
- Solution: Reinstall Python and check "Add Python to PATH"
- Alternative: Add Python manually to PATH in System Environment Variables

**2. "Node is not recognized as an internal or external command"**
- Solution: Reinstall Node.js
- Alternative: Add Node.js to PATH manually

**3. "Permission denied" errors**
- Solution: Run Command Prompt as Administrator
- Alternative: Change folder permissions

**4. "Module not found" errors**
- Solution: Ensure virtual environment is activated
- Run: `venv\Scripts\activate` before running Python commands

**5. Port already in use**
- Solution: Kill existing processes or use different ports
- Check running processes: `netstat -ano | findstr :5000`
- Kill process: `taskkill /PID <process_id> /F`

**6. Antivirus blocking installation**
- Solution: Temporarily disable antivirus during setup
- Add project folder to antivirus exclusions

### Performance Optimization for Windows

**1. Windows Defender Exclusions**
Add these folders to Windows Defender exclusions:
- `C:\blood_donation_system\backend\venv\`
- `C:\blood_donation_system\frontend\node_modules\`

**2. PowerShell Execution Policy**
If you encounter PowerShell script execution issues:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**3. Virtual Memory Settings**
For better performance with large datasets:
- Increase virtual memory (pagefile) size
- Recommended: 16GB if you have 8GB RAM

## 📁 Windows File Structure

```
C:\blood_donation_system\
├── backend\
│   ├── venv\                 # Python virtual environment
│   ├── src\                  # Backend source code
│   ├── models\               # Trained AI models
│   ├── data\                 # Data files
│   └── requirements.txt      # Python dependencies
├── frontend\
│   ├── node_modules\         # Node.js dependencies
│   ├── src\                  # Frontend source code
│   └── package.json          # Node.js configuration
├── docs\                     # Documentation
├── analysis\                 # Analysis charts and reports
├── setup_windows.bat         # Windows setup script
├── start_backend.bat         # Backend startup script
├── start_frontend.bat        # Frontend startup script
└── README.md                 # Main documentation
```

## 🔒 Windows Security Considerations

### Firewall Settings
Windows may prompt to allow Python and Node.js through the firewall:
- ✅ Allow Python through Windows Firewall
- ✅ Allow Node.js through Windows Firewall
- ✅ Allow on both Private and Public networks for development

### User Account Control (UAC)
- Run Command Prompt as Administrator for initial setup
- Regular user permissions are sufficient for running the application

## 🎯 Windows-Specific Features

### Desktop Shortcuts
Create desktop shortcuts for easy access:

**Backend Shortcut:**
- Target: `C:\Windows\System32\cmd.exe`
- Arguments: `/k "cd /d C:\blood_donation_system && start_backend.bat"`

**Frontend Shortcut:**
- Target: `C:\Windows\System32\cmd.exe`
- Arguments: `/k "cd /d C:\blood_donation_system && start_frontend.bat"`

### Task Scheduler (Optional)
Set up automatic startup using Windows Task Scheduler:
1. Open Task Scheduler
2. Create Basic Task
3. Set trigger (e.g., at startup)
4. Set action to run `start_backend.bat`

## 📊 Performance Monitoring on Windows

### Task Manager Monitoring
Monitor system performance:
- **CPU Usage**: Should be <50% during normal operation
- **Memory Usage**: Backend ~500MB, Frontend ~200MB
- **Disk Usage**: Minimal after initial setup

### Windows Performance Toolkit
For advanced monitoring:
- Use Windows Performance Monitor (perfmon)
- Monitor Python.exe and Node.js processes
- Track memory and CPU usage over time

## 🔄 Updates and Maintenance

### Updating the System
```cmd
# Update Python packages
cd backend
venv\Scripts\activate
pip install --upgrade -r requirements.txt

# Update Node.js packages
cd ..\frontend
npm update
```

### Backup and Restore
**Backup important files:**
- `backend\database\app.db` (database)
- `backend\models\*.pkl` and `backend\models\*.h5` (trained models)
- Configuration files

**Restore procedure:**
1. Run setup_windows.bat
2. Replace database and model files
3. Restart application

## 🆘 Getting Help

### Windows-Specific Support
- **GitHub Issues**: Tag issues with "Windows"
- **Discord**: #windows-support channel
- **Email**: windows-support@bloodwarriors.ai

### Useful Windows Commands
```cmd
# Check Python installation
python --version
pip --version

# Check Node.js installation
node --version
npm --version

# Check running processes
tasklist | findstr python
tasklist | findstr node

# Check port usage
netstat -ano | findstr :5000
netstat -ano | findstr :5174

# System information
systeminfo
```

## ✅ Windows Setup Checklist

- [ ] Python 3.11+ installed with PATH
- [ ] Node.js 20.x LTS installed
- [ ] Git for Windows installed
- [ ] Project downloaded/cloned
- [ ] setup_windows.bat executed successfully
- [ ] Backend starts without errors
- [ ] Frontend starts without errors
- [ ] Can access http://localhost:5174
- [ ] Can access http://localhost:5000/api/gemini/status
- [ ] All tests pass (optional)

## 🎉 Success on Windows!

If everything is working correctly, you should see:

1. **Backend Console**: Flask server running on port 5000
2. **Frontend Console**: Vite dev server running on port 5174
3. **Browser**: Blood Warriors dashboard loads successfully
4. **API**: Status endpoint returns JSON response

**Congratulations! You're now running the Blood Warriors AI system on Windows!**

---

**Windows-Specific Support**: For Windows-related issues, please include your Windows version, Python version, and Node.js version when seeking help.

