# conf.py - Minimal-Konfiguration
import os
import sys

# Projekt-Informationen
project = 'TYPO3 Extension Bib'
copyright = '2015, Ingo Pfennigstorf'
author = 'Ingo Pfennigstorf'
version = '1.6.1'
release = '1.6.1'

# WICHTIG: Hier muss der Name Ihrer Hauptdatei stehen (ohne .rst)
# Bei TYPO3 ist das meistens 'Index' (großgeschrieben) oder 'index' (klein).
# Prüfen Sie genau, wie die Datei heißt!
master_doc = 'index'

# Extensions laden
extensions = []

# Templates und Statische Dateien (können leer bleiben für Standard-Look)
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Design für HTML (Standard ist 'alabaster', 'rtd_theme' ist schöner, muss aber installiert sein)
#html_theme = 'alabaster'

try:
    import sphinx_typo3_theme
    html_theme = 'sphinx_typo3_theme'
    extensions.append("sphinx_typo3_theme")
except ImportError:
    html_theme = 'alabaster'