"""Sphinx configuration."""

project = "Uv Hypermodern Python"
author = "bosd"
copyright = "2025, bosd"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "shibuya"
