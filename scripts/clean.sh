# Delete all auxiliary files (*.aux, *.bbl, *.log, *.out)
find . -name "*.aux" -type f -delete
find . -name "*.bbl" -type f -delete
find . -name "*.log" -type f -delete
find . -name "*.out" -type f -delete

find . -name "seminararbeit.blg" -type f -delete
find . -name "seminararbeit.run.xml" -type f -delete
find .  -name "seminararbeit.toc" -type f -delete
find .  -name "seminararbeit.bcf" -type f -delete
