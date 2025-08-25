@echo off
title Claude 4 Sonnet Hack for Cursor
color 0A

echo.
echo =====================================
echo   Claude 4 Sonnet Hack for Cursor
echo =====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH!
    echo Please install Python 3.6+ and add it to your PATH.
    pause
    exit /b 1
)

REM Check if hack_claude4.py exists
if not exist "hack_claude4.py" (
    echo ERROR: hack_claude4.py not found!
    echo Please make sure hack_claude4.py is in the same directory as this batch file.
    pause
    exit /b 1
)

echo Running Claude 4 Sonnet hack...
echo.
echo This will:
echo - Set token limit to 200,000 for Claude 4 Sonnet
echo - Enable high thinking level
echo - Add "HACKED" styling to Claude 4 Sonnet
echo.

REM Run the Python script with default settings
python hack_claude4.py --token-mode claude4_only --ui-style gradient

if errorlevel 1 (
    echo.
    echo ERROR: Hack failed! Check the error messages above.
    echo.
) else (
    echo.
    echo SUCCESS: Claude 4 Sonnet hack completed!
    echo.
    echo IMPORTANT: You need to restart Cursor for changes to take effect.
    echo.
)

echo Press any key to exit...
pause >nul 