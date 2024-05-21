@echo off
setlocal enabledelayedexpansion

set "file_paths=seminararbeit.tex preambel.tex design-patterns.tex responsive-webdesign.tex"
set "script_path=scripts\build.bat"

set "first_run=1"

:watch
for %%f in (%file_paths%) do (
    for /f %%t in ('powershell -Command "(Get-Item '%%f').LastWriteTime.ToString('yyyyMMddHHmmss')"') do (
        rem echo Checking file '%%f' with timestamp %%t compared to !last_modified[%%f]!...
        if "!last_modified[%%f]!" neq "%%t" (
            if not defined first_run (
                echo File '%%f' has been modified. Running script '%script_path%'...
                call "%script_path%" -no-biber
            )
            set "last_modified[%%f]=%%t"
        )
    )
)
set "first_run="
timeout /t 1 >nul
goto watch