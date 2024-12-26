"""Sphinx configuration."""
project = "Hypermodern Simple Math Game"
author = "Derek R. Neilson"
copyright = "2024, Derek R. Neilson"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
