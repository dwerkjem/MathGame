from typing import List

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Simple math game"
copyright = "2024, Derek R. Neilson"
author = "Derek R. Neilson"
release = "0.0.1"

# -- General configuration ---------------------------------------------------

extensions: List[str] = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    # Add other extensions here
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "haiku"
html_static_path = ["_static"]

# -- Options for LaTeX output ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

latex_engine = "pdflatex"

latex_elements = {
    "papersize": "letterpaper",
    "pointsize": "10pt",
    "figure_align": "htbp",
}

text_newlines = "unix"
