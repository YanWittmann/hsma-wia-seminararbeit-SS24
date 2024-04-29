#!/bin/bash

clear

# Compile the seminararbeit with pdflatex twice (for references)
pdflatex seminararbeit
if [ $? -ne 0 ]; then
  echo "Error occurred during first pdflatex compilation. Exiting."
  exit 1
fi
pdflatex seminararbeit
if [ $? -ne 0 ]; then
  echo "Error occurred during second pdflatex compilation. Exiting."
  exit 1
fi

# Run Biber to process the bibliography
biber seminararbeit
if [ $? -ne 0 ]; then
  echo "Error occurred during Biber processing. Exiting."
  exit 1
fi

# Compile the seminararbeit again with pdflatex to incorporate the bibliography
pdflatex seminararbeit
if [ $? -ne 0 ]; then
  echo "Error occurred during third pdflatex compilation. Exiting."
  exit 1
fi

# Delete all auxiliary files (*.aux, *.bbl, *.log, *.out)
find . -name "*.aux" -type f -delete
find . -name "*.bbl" -type f -delete
find . -name "*.log" -type f -delete
find . -name "*.out" -type f -delete

find . -name "seminararbeit.blg" -type f -delete
find . -name "seminararbeit.run.xml" -type f -delete
find .  -name "seminararbeit.toc" -type f -delete
find .  -name "seminararbeit.bcf" -type f -delete

echo "Seminararbeit compilation complete and auxiliary files deleted."

