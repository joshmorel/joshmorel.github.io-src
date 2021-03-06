#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Josh Morel'
SITENAME = u'Josh Morel'
SITEURL = ''

#################### Content/Output Paths ####################

PATH = 'content'
OUTPUT_PATH = 'dist/'
DELETE_OUTPUT_DIRECTORY = True

EXTRA_PATH_METADATA = {'images/favicon.ico': {'path': 'favicon.ico'},}

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('github', 'http://github.com/joshmorel'),
          ('linkedin', 'https://ca.linkedin.com/in/josh-morel-94373221'),
          )

DEFAULT_PAGINATION = False


#################### Theme-Specific Settings #################

THEME = 'pelican-bootstrap3'
DISQUS_SITENAME = 'joshmorel'
CC_LICENSE = 'CC-BY-SA'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

#################### Plugin-Specific Settings #################

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['tag_cloud', 'series', 'i18n_subsites']
TAG_CLOUD_SORTING = 'alphabetically'
