@echo off

echo Installation des extensions Python nécessaires pour le bon fonctionnement des scripts...
echo.

REM Liste des packages à installer
set PACKAGES=python-nmap scapy requests googlesearch-python geoip2 flask whois fpdf jinja2 zxcvbn

REM Boucle pour installer chaque package
for %%i in (%PACKAGES%) do (
    echo Installation de %%i ...
    pip install %%i
    echo.
)

echo Installation terminée.
pause
