#!/bin/bash

OUTPUT=output

mkdir -p $OUTPUT

pelican content -o $OUTPUT -s pelicanconf.py

# change cite to kbd lable
sed -i.bk 's|<cite>|<kbd>|g;s|</cite>|</kbd>|g' output/posts/2015/08/20/useful-intellij-ide-shortcuts-on-mac-os-x/index.html

ghp-import $OUTPUT

git push \
    -f git@github.com:caesar0301/caesar0301.github.io.git \
    gh-pages:master
