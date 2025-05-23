# Configuration file for the Sphinx documentation builder.
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

import os
import sys

try:
    from unittest.mock import MagicMock
except ImportError:
    from mock import Mock as MagicMock


class Mock(MagicMock):

    @classmethod
    def __getattr__(cls, name):
        return MagicMock()


MOCK_MODULES = ["xarray", "dask", "dask.array", "dask.array.core"]
sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx', 'sphinx.ext.mathjax'
]

intersphinx_mapping = {
    'python': ('http://docs.python.org/3/', None),
    'xarray': ('http://xarray.pydata.org/en/stable/', None),
}

napoleon_use_admonition_for_examples = True
napoleon_include_special_with_doc = True

autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'uxarray'

import datetime

current_year = datetime.datetime.now().year
copyright = u'{}, Uxarray'.format(current_year)
author = u'UXARRAY'


# The version info for the project being documented
def read_version():
    for line in open('../meta.yaml').readlines():
        index = line.find('set version')
        if index > -1:
            return line[index + 15:].replace('\" %}', '').strip()


# The short X.Y version.
version = read_version()

# The full version, including alpha/beta/rc tags.
release = read_version()

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

on_rtd = os.environ.get('READTHEDOCS') == 'True'
if on_rtd:
    html_theme = 'default'
else:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
# html_title = u'uxarray v0.0.1'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = '_static/images/nsf.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = 'uxarraydoc'

autodoc_typehints = 'none'


# Allow for changes to be made to the css in the theme_overrides file
def setup(app):
    app.add_css_file('theme_overrides.css')
