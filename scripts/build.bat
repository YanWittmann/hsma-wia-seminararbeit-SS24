@echo off
rem cls

echo Building document

set NO_BIBER=false

rem Check if the parameter "-no-biber" is provided
if "%1" == "-no-biber" (
  set NO_BIBER=true
)

echo Building document, biber inactive: %NO_BIBER%

rem Compile the seminararbeit with pdflatex twice (for references)
pdflatex seminararbeit.tex
if errorlevel 1 (
  echo Error occurred during first pdflatex compilation. Exiting.
  exit /b 1
)

rem check if the "-no-biber" parameter is provided and if so, stop here
if "%NO_BIBER%" == "true" (
  goto :skip_biber
)

rem Run Biber to process the bibliography
biber seminararbeit
if errorlevel 1 (
  echo Error occurred during Biber processing. Exiting.
  exit /b 1
)

rem Compile the seminararbeit again with pdflatex to incorporate the bibliography
pdflatex seminararbeit.tex
if errorlevel 1 (
  echo Error occurred during third pdflatex compilation. Exiting.
  exit /b 1
)

pdflatex seminararbeit.tex
if errorlevel 1 (
  echo Error occurred during second pdflatex compilation. Exiting.
  exit /b 1
)

:skip_biber

echo Document built successfully.
