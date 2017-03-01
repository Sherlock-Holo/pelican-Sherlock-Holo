#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sherlock Holo'
SITENAME = "夏洛克狼的传记"
SITEURL = ''
PICTURESURL = 'https://c1.staticflickr.com'

# LOGO
USER_LOGO_URL = PICTURESURL + '/1/603/33164043315_e7e630d5fc_m.jpg'
USER_AVATAR_URL = PICTURESURL + '/1/603/33164043315_e7e630d5fc_m.jpg'
# CDN
#USE_CDN = True

# color
#PRIMARY_COLOR = 'teal'
#ACCENT_COLOR = 'Light Blue'


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
# LINKS = (('Pelican', 'https://getpelican.com/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/Sherlock-Holo'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = './themes/pelican-material'

# material theme
from functools import partial
JINJA_FILTERS = {
    'sort_by_article_count': partial(
        sorted,
        key=lambda tags: len(tags[1]),
        reverse=True)} # reversed for descending order

#plugin

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['gzip_cache']
