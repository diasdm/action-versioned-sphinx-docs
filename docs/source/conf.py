# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Versioned Sphinx docs'
copyright = '2023, David Dias'
author = 'David Dias'
version = os.getenv("VERSION", default="TODO")

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.todo",
    "sphinx_mdinclude",
]

templates_path = ['_templates']
exclude_patterns = []

todo_include_todos = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_js_files = ["versions.js"]

html_context = {}
# used in versions.html
html_context["current_version"] = version

# -- Theme options -----------------------------------------------------------
# https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html#configuration
html_context["display_github"] = True
html_context["github_user"] = "diasdm"
html_context["github_repo"] = "action-versioned-sphinx-docs"
branch = version if version == "main" else f"releases/{version}"
html_context["github_version"] = f"{branch}/docs/source/"
