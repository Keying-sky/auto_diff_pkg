nbsphinx_kernel_name = 'python3'

import sphinx_rtd_theme

project = 'dual_autodiff'
copyright = '2024, Keying Song'
author = 'Keying Song'
release = '0.0.0beta0'


extensions = [
	'nbsphinx',
	'sphinx.ext.mathjax',
	'sphinx_rtd_theme',
    'sphinx_gallery.load_style',  
    'sphinx.ext.githubpages',
]


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'tutorial_notebooks/tutorial*/*_empty.ipynb']


html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

master_doc = 'index'

highlight_language = 'python3'

nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg', 'pdf'}",
    "--InlineBackend.rc={'figure.dpi': 96}",
]


secnumber_suffix = '' 

nbsphinx_execute = 'auto'  


source_suffix = {
    '.rst': 'restructuredtext'
}

