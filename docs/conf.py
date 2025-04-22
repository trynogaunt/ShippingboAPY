# Configuration file for the Sphinx documentation builder.

import os
import sys
from datetime import datetime

# -- Path setup -----------------------------------------------------
sys.path.insert(0, os.path.abspath(".."))

# -- Project information --------------------------------------------
project = 'ShippingboAPY'
author = 'Tryno'
copyright = f'{datetime.now().year}, {author}'
release = '0.1.0'

# -- General configuration ------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output ----------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Autodoc configuration ------------------------------------------
autodoc_member_order = 'bysource'
autodoc_typehints = 'description'