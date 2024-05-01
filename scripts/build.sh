#!/bin/bash

clear

# Check if the parameter "-no-biber" is provided
NO_BIBER=false
if [ "$1" == "-no-biber" ]; then
  NO_BIBER=true
fi

echo "Building document, biber inactive: $NO_BIBER"

# Compile the seminararbeit with pdflatex twice (for references)
pdflatex seminararbeit
if [ $? -ne 0 ]; then
  echo "Error occurred during first pdflatex compilation. Exiting."
  exit 1
fi

# Check if the "-no-biber" parameter is provided and if so, stop here
if [ "$NO_BIBER" = true ]; then
  echo "Document built successfully (without Biber)."
  exit 0
fi

# Run Biber to process the bibliography
biber seminararbeit
if [ $? -ne 0 ]; then
  echo "Error occurred during Biber processing. Exiting."
  exit 1
fi

pdflatex seminararbeit
if [ $? -ne 0 ]; then
  echo "Error occurred during second pdflatex compilation. Exiting."
  exit 1
fi

# Compile the seminararbeit again with pdflatex to incorporate the bibliography
pdflatex seminararbeit
if [ $? -ne 0 ]; then
  echo "Error occurred during third pdflatex compilation. Exiting."
  exit 1
fi

echo "Document built successfully."
