#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

## Site info
AUTHOR = u'Xiaming Chen'
SITENAME = u'StaTrek'
SITESUBTITLE = u'为，可为，可不为！'
SITEURL = 'http://xiaming.me'
LOCALE = "en_US.UTF-8"

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

## Theme
THEME = "themes/zurb-F5-basic"
COVER_IMG_URL = "images/galaxy-universe-banner-v.jpg"
DISQUS_SITENAME = "hsiamincom"
GOOGLE_ANALYTICS = "UA-36744847-3"
# MENUITEMS = (('About', 'pages/about'),
#              ('Publications', 'pages/publications'),
#              ('Researches', 'pages/researches'),
#              ('Projects', 'pages/projects'),
#              ('Contact', 'pages/contact'))

## Static files
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
	'extra/favicon.ico': {'path': 'favicon.ico'},
	'extra/CNAME': {'path': 'CNAME'},
}

## Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ['gravatar']

## Gravatar settings
AUTHOR_EMAIL = "chenxm35@gmail.com"

## Social widgets
SOCIAL = (('Github', 'https://github.com/caesar0301/'),
          ('Twitter', 'https://twitter.com/xiamingc'),
          ('Weibo', 'http://weibo.com/fuckinmylife'),
          ('LinkedIn', 'https://www.linkedin.com/in/xiamingc'),
          ('OMNILab', 'http://omnilab.sjtu.edu.cn'),
          ('RSS', 'http://xiaming.me/feeds/all.atom.xml'))
