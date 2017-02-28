#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sherlock Holo'
SITENAME = "Sherlock Holo's Blog"
SITEURL = ''
PICTURESURL = 'https://c1.staticflickr.com'

# LOGO
USER_LOGO_URL = PICTURESURL + '/1/603/33164043315_e7e630d5fc_m.jpg'
USER_AVATAR_URL = PICTURESURL + '/1/603/33164043315_e7e630d5fc_m.jpg'
# CDN
#USE_CDN = True

# color
#PRIMARY_COLOR = 'Green'
#ACCENT_COLOR = 'Green'


PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'

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
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/Sherlock-Holo'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = './themes/material'
