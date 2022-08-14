@echo off
"C:\Python374\python.exe" "C:\adrd\initializeAdrFields.py"
timeout /t 2
"C:\Python374\python.exe" "C:\adrd\adrd.py"
pause