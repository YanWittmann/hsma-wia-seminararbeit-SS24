# HSMA Wissenschaftliches Arbeiten SS2024 Seminararbeit

Dieses Repository enthält die Seminararbeit von Yan Wittmann zum Thema "Dashboardgestaltung auf Mobilgeräten" im Rahmen
des Pflichtmoduls "Wissenschaftliches Arbeiten" im Sommersemester 2024 an der Hochschule Mannheim.

## Bauen des Dokuments

Das Skript `scripts/build.sh` / `scripts/build.bat` baut das Dokument.
Im Nachhinein kann mit `scripts/clean.sh` / `scripts/clean.bat` das Verzeichnis wieder aufgeräumt werden.
Es werden dabei pdflatex und biber verwendet.
Ansonsten können auch einfach diese Befehle ausgeführt werden:

```bash
pdflatex seminararbeit
biber seminararbeit
pdflatex seminararbeit
pdflatex seminararbeit
```

Convenience-Scripts für das automatische Bauen bei Änderungen sind in `scripts/watch.sh` / `scripts/watch.bat` zu
finden.

## Installation der Abhängigkeiten

Ich musste zusätzlich zu pdflatex folgende Pakete installieren:

```bash
sudo apt install texlive-publishers
sudo apt install texlive-science
sudo apt install texlive-extra-utils
sudo apt-get install texlive-bibtex-extra biber
sudo apt-get install texlive-lang-german
```
