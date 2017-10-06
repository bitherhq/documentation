# -*- coding: utf-8 -*-

import sys
import os
import shlex

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'Bither Documentation'
copyright = u'2017, Bither community'
author = u'Bither community'
version = u'0.1'
release = u'0.1'
language = None
exclude_patterns = ['_build']
pygments_style = 'sphinx'
todo_include_todos = True
html_theme = 'sphinx_rtd_theme'
htmlhelp_basename = 'homesteadguidedoc'

latex_elements = {
'papersize': 'a4paper',
'pointsize': '10pt',
}
latex_documents = [
  (master_doc, 'homesteadguide.tex', u'Bither Documentation',
   u'Bither community', 'manual'),
]
man_pages = [
    (master_doc, 'Documentation', u'Bither Documentation',
     [author], 1)
]
texinfo_documents = [
  (master_doc, 'documentation', u'Bither Documentation',
   author, 'documentation', 'One line description of project.',
   'Miscellaneous'),
]
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
epub_exclude_files = ['search.html']

