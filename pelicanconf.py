#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

## Site info
AUTHOR = u'Xiaming Chen'
SITENAME = u'InnoTrek'
#SITESUBTITLE = u"Welcome to Xiaming Chen's Home"
SITEURL = 'http://xiaming.me'
LOCALE = "en_US.UTF-8"

## Gravatar settings
AUTHOR_EMAIL = "chenxm35@gmail.com"

## Basic settings
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = u'en'
DEFAULT_PAGINATION = 6
DEFAULT_DATE = (2012, 03, 02, 14, 01, 01)
RELATIVE_URLS = True
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
DISPLAY_PAGES_ON_MENU = True
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

## Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ['gravatar']

THEME = "pelican-themes/fresh"

## Builtin
DISQUS_SITENAME = "xiamingdotme"
GOOGLE_ANALYTICS = "UA-36744847-3"
MENUITEMS = ()
GITHUB_URL = 'http://github.com/caesar0301'
SOCIAL = (('Github', 'https://github.com/caesar0301/'),
          ('Twitter', 'https://twitter.com/xiamingc'),
          ('Weibo', 'http://weibo.com/fuckinmylife'),
          ('LinkedIn', 'https://www.linkedin.com/in/xiamingc'),
          ('OMNILab', 'http://omnilab.sjtu.edu.cn'),
          ('RSS', 'http://xiaming.me/feeds/all.atom.xml'))

## Theme specific
COVER_IMG_URL = "images/galaxy-universe-banner-v.jpg"
GOOGLE_CUSTOM_SEARCH = '018436494580770914622:g1czldkqcfm'
SHARETHIS_PUB_KEY = '106f5e17-e570-445e-84fd-d442231ba3c0'
HIDE_CATEGORIES_FROM_MENU = True

## Static files
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
	'extra/favicon.ico': {'path': 'favicon.ico'},
	'extra/CNAME': {'path': 'CNAME'},
	'extra/mycv_ch.pdf': {'path': 'mycv_ch.pdf'},
	'extra/mycv_en.pdf': {'path': 'mycv_en.pdf'}
}

