# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Reltrans'
copyright = '2025, Guglielmo Mastroserio, Adam Ingram, Matteo Lucchini, Ben Ricketts'
author = 'Guglielmo Mastroserio, Adam Ingram, Matteo Lucchini, Ben Ricketts'
release = '2.3'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'nbsphinx', 
    'sphinx.ext.autodoc',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

def setup(app):
    app.add_css_file('tweak_theme.css')

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'navigation_with_keys': True,
}

html_sidebars = {
    '**': [
        'about.html',
        #'globaltoc.html',
        'localtoc.html',
        #'navigation.html',
        'searchbox.html',
        #'sourcelink.html',
    ]
}

html_static_path = ['_static']
