@echo off

echo | set /p="Project contains "
set /a i=0
for /R %%F in (*.py) do (
  for /F "tokens=*" %%A in (%%F) do (
    call :countline %%A
    if errorlevel 1 (
      set /a i+=1
    )
  )
)
echo %i% lines of code
echo.

echo Executing all tests:
dir /b *_test.py | py.test

goto :eof

:countline
set line=%1
set line=%line:~0,1%
set line=%line:"=quote%
set result=0
if not "%line%" == "#" (
  set result=1
)
exit /b %result%

