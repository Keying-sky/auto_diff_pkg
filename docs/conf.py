# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

#import os
#import sys
#sys.path.insert(0, os.path.abspath('../'))

# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

nbsphinx_kernel_name = 'python3'

import sphinx_rtd_theme

# -- Project information -----------------------------------------------------
project = 'dual_autodiff'
copyright = '2024, Keying Song'
author = 'Keying Song'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
	'nbsphinx',
	'sphinx.ext.mathjax',
	'sphinx_rtd_theme',
    'sphinx_gallery.load_style',  # load CSS for gallery (needs SG >= 0.6)
    'sphinx.ext.githubpages',
]

'''
sphinx_gallery_conf = {
    'examples_dirs': '../notebooks',  # 存放 .ipynb 文件的路径（相对于 conf.py）
    'gallery_dirs': 'auto_examples',  # 输出生成的文档路径（相对于 docs/）
}
'''
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'tutorial_notebooks/tutorial*/*_empty.ipynb']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

master_doc = 'index'

highlight_language = 'python3'

nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg', 'pdf'}",
    "--InlineBackend.rc={'figure.dpi': 96}",
]


# Disable section numbering
secnumber_suffix = ''  # No suffix means no section numbers
# numfig = False  # Disable figure/table numbering if you don't need them

# 可选：避免 notebook 执行超时
nbsphinx_execute = 'auto'  # 或 'always', 'auto'


source_suffix = {
    '.rst': 'restructuredtext'
}

