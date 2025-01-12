@echo off

set SCRIPT_DIR=%~dp0

set SCRIPT_DIR=%SCRIPT_DIR:~0,-1%

set PYTHON_PATH=%SCRIPT_DIR%\Python_package

%PYTHON_PATH%\python.exe %SCRIPT_DIR%\mplee_run.py %*

