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

echo "Seminararbeit compilation complete."

