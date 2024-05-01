@echo off
setlocal enabledelayedexpansion

set "file_paths=seminararbeit.tex preambel.tex"
set "script_path=scripts\build.bat"

for %%f in (%file_paths%) do (
    set "last_modified[%%f]=0"
)

:watch
for %%f in (%file_paths%) do (
    for /f "delims=" %%t in ('powershell -Command "(Get-Item '%%f').LastWriteTime.Ticks"') do (
        if !last_modified[%%f]! lss %%t (
            echo File '%%f' has been modified. Running script '%script_path%'...
            cmd /c "%script_path%" -no-biber
            set "last_modified[%%f]=%%t"
        )
    )
)
timeout /t 1 >nul
goto watch
