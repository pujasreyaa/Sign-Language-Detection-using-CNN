@echo off
echo Setting up Sign Language Detection Project...

REM Check if conda is available
where conda >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Conda not found. Please install Anaconda or Miniconda first.
    pause
    exit /b 1
)

REM Create conda environment
echo Creating conda environment...
conda create -n tf python=3.7.9 -y

REM Activate environment
echo Activating environment...
call conda activate tf

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Run migrations
echo Running Django migrations...
python manage.py makemigrations
python manage.py migrate

REM Start server
echo Starting Django server...
echo.
echo Project will be available at: http://127.0.0.1:8000/
echo.
python manage.py runserver

pause