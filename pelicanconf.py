#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITEURL = '/blog'
OUTPUT_PATH = 'output/blog'
PAGE_URL = '../{slug}.html'
PAGE_SAVE_AS = '../{slug}.html'

STATIC_PATHS = ['images', 'pdfs']

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [('Home', '/'), 
             ('Research', '/research.html'),
             ('Publications', '/publications.html'),
             ('Teaching', '/teaching.html'),
             ('Software', '/software.html'),
             #('Blog', '/blog/'),
             ('Blog', 'https://scottyhq.github.io/blog'),
             ]


AUTHOR = 'Scott Henderson'
SITENAME = 'Scott Henderson'
#SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('eScience Institute', 'http://escience.washington.edu'),
        ('UW ESS', 'http://www.ess.washington.edu'),
        ('UniAndes Geociencias', 'http://geociencias.uniandes.edu.co/index.php/home'),
        #('Smithsonian GVP', 'http://volcano.si.edu/'),
        #('USGS VH', 'https://volcanoes.usgs.gov/index.html'),
        #('Cornell EAS', 'http://www.eas.cornell.edu'),
        )

# Social widget
# Social widget
SOCIAL = (('GitHub', 'https://github.com/scottyhq'),
          ('LinkedIn', 'https://www.linkedin.com/in/scott-henderson-1a5666b4'),)

#DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
