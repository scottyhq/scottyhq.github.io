#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# To keep static homepage and blog under separate tab
#SITEURL = '/blog'
#OUTPUT_PATH = 'output/blog'
#PAGE_URL = '../{slug}.html'
#PAGE_SAVE_AS = '../{slug}.html'

STATIC_PATHS = ['images', 'pdfs', 'extra/favicon.ico']

EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'},}

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [('Home', '/index.html'), 
             ('Research', '/pages/research.html'),
             ('Publications', '/pages/publications.html'),
             ('Teaching', '/pages/teaching.html'),
             ('Software', '/pages/software.html'),
             ('Blog', '/pages/blog.html'),
             #('Blog', 'https://scottyhq.github.io/blog'),
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

# Disable tag -related pages for non-blog site
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

LOAD_CONTENT_CACHE = False

# Blogroll
LINKS = (('UW eScience Institute', 'https://escience.washington.edu'),
        ('UW Earth & Space Sciences', 'https://www.ess.washington.edu'),
        ('UniAndes Geociencias', 'https://geociencias.uniandes.edu.co/index.php/home'),
        ('Pangeo Project', 'https://pangeo.io'),
        ('Pangeo Blog', 'https://medium.com/pangeo'),
        #('Smithsonian GVP', 'https://volcano.si.edu/'),
        #('USGS VH', 'https://volcanoes.usgs.gov/index.html'),
        #('Cornell EAS', 'https://www.eas.cornell.edu'),
        ('PNW Seismic Network', 'https://pnsn.org'),
        #('PANGA', 'https://www.geodesy.cwu.edu/'),
        ('UNevada Geodetic Lab', 'https://geodesy.unr.edu/'),
        ('Alaska Satellite Facility', 'https://www.asf.alaska.edu'),
        #('UNAVCO', 'https://www.unavco.org/'),
        ('Pelican Website Builder', 'https://docs.getpelican.com/en/stable'),
        )

# Social widget
# Social widget
SOCIAL = (('GitHub', 'https://github.com/scottyhq'),
          ('Twitter', 'https://twitter.com/scotty_h_q'),
#          ('LinkedIn', 'https://www.linkedin.com/in/scott-henderson-1a5666b4'),
         )

#DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "notmyidea"

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.attr_list': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

