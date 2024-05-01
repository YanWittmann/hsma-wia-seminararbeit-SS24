@echo off

set "file_paths=seminararbeit.tex preambel.tex"
set "script_path=scripts\build.bat"

:watch
for %%f in (%file_paths%) do (
    for /f "delims=" %%t in ('powershell -Command "Get-Item '%%f' | Select-Object -ExpandProperty LastWriteTime"') do (
        if not defined last_modified[%%f] (
            set "last_modified[%%f]=%%t"
        ) else if "!last_modified[%%f]!" neq "%%t" (
            echo File '%%f' has been modified. Running script '%script_path%'...
            cmd /c "%script_path%" -no-biber
            set "last_modified[%%f]=%%t"
        )
    )
)
timeout /t 1 >nul
goto watch
