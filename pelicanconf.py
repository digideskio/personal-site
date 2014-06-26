#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

## Site info
AUTHOR = u'Xiaming Chen'
SITENAME = u'Xiaming Chen'
SITEURL = 'http://hsiamin.com'
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
THEME = "themes/pure"
COVER_IMG_URL = "http://www.hdwallpapers.in/walls/galaxy_universe-normal.jpg"
DISQUS_SITENAME = "hsiamincom"
#GOOGLE_ANALYTICS = "UA-000000-00"
MENUITEMS = (('About', 'pages/about'),
             ('Publications', 'pages/publications'),
             ('Researches', 'pages/researches'),
             ('Projects', 'pages/projects'),
             ('Contact', 'pages/contact'))

## Static files
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

## Plugins
PLUGIN_PATH = "plugins"
PLUGINS = ['gravatar']

## Gravatar settings
AUTHOR_EMAIL = "caesar0301@163.com"

## Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

## Social widgets
SOCIAL = (('github', 'https://github.com/caesar0301/'),
          ('weibo', 'http://weibo.com/fuckinmylife'),
          ('rss', 'http://hsiamin.com/feeds/all.atom.xml'))
