#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Adam Fast'
SITENAME = 'Adam Fast - Software Developer'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
    ('GitHub', 'https://github.com/adamfast'),
    ('LinkedIn', 'https://linkedin.com/in/adamfast'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Theme settings
THEME = 'themes/simple'

# Display settings
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Static paths
STATIC_PATHS = ['images', 'extra']

# Direct templates
DIRECT_TEMPLATES = ['index']

# Page settings
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Disable articles, tags, categories - this is a single page site
ARTICLE_PATHS = []
ARTICLE_SAVE_AS = ''
ARTICLE_URL = ''
ARCHIVES_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''
AUTHORS_SAVE_AS = ''