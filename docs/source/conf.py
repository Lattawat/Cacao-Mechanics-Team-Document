import datetime
import string
import sys
import os

# Configuration file for the Sphinx documentation builder.

# Package information
project = "CACAO@HOME Robot"
author = "Cacao Team"
copyright = f"2022-{datetime.date.today().year}, {author}"

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]
sphinx_tabs_valid_builders = ['linkcheck']
sphinx_tabs_disable_tab_closing = True
sphinx_tabs_disable_css_loading = True
source_suffix = ".rst"
pygments_style = "sphinx"

master_doc = "index"
language = 'en'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
