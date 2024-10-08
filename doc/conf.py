# Configuration file for the Sphinx documentation builder.

# For exercise tutorial from Coderefinery: https://coderefinery.github.io/documentation/sphinx/
# For exercise GitHubAction to deploy the documentation automatically, when a new Git commit is made
# https://coderefinery.github.io/documentation/gh_workflow/#exercise-deploy-sphinx-documentation-to-github-pages
# This will generate HTML documentation page here: https://go5it.github.io/code_refinery_sphinx_documentation_example/


# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Example'
copyright = 'workshop participant'
author = 'workshop participant'
release = '0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# this is a trick to make sphinx find the modules in the parent directory
import os
import sys
# sys.path.insert(0, os.path.abspath(".")) # Same folder as index.rst
sys.path.insert(0, os.path.abspath('../src/code'))  # Python to Python files

extensions = ['myst_parser', "sphinx.ext.autodoc"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
