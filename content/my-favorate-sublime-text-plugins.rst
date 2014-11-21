Favorite Sublime Text Plugins in My Toolkit
============================================

:date: 2014-10-14
:author: Xiaming Chen
:category: Tools
:tags: editor, plugins

`Sublime Text`_ is one of my favorite editors (emacs, of course, as another)
for daily programming, writing tasks. One of its appealing features is the
infinite possibility to bring you to unknown lands with plenty of extensions
(or plugins) via its package manager, i.e., `Package Control`_. If you can not
find the functionality that you want, a encouraging way is write your own and
contribute it to this world.

Here, I give a list of extensions in my daily usage. Before installing, you
should first make sure that `Package Control`_ is enabled. It's simple to
`paste && run <https://sublime.wbond.net/installation>`_ in the editor's
console to install it. And this may be the only one plugin to install outside
ST's screen.

After the installation of `Package Control`_, you can activate the package
manager using ``cmd+shift+P`` (Mac) or ``ctrl+shift+P`` (PC) then ``Package
Control``.

.. _Package Control: https://sublime.wbond.net/
.. _Sublime Text: http://www.sublimetext.com/


Git
-----------------

Git invented by Linus Torvalds has brought up a storm over the programming
land. `GitGutter <https://github.com/jisaacks/GitGutter>`_ can be the one you
don't want to give up ever. Of course, another `Git <https://github.com/kemayo
/sublime-text-git>`_ is also available to meet your taste.


Python
-----------------

Python is my first and mostly-used language in past three years. But the
Sublime does not let me down for the flexible python programming. A `nice blog
written by Daniel <http://dbader.org/blog/setting-up-sublime-text-for-python-
development>`_ gives a more detailed intro for starters.


Pig
-----------------

The package `Apache Pig <https://github.com/chrislongo/Pig>`_ gives support of
Pig syntax and local running via the embedded console. I love this tool as it
make my pig debugging more easily.


Markup languages
-----------------

Markdown and reStructuredText are two popular markup syntax in plain editing.
Two basic requirements are syntax highlighting and preview (or HTML
generation). For syntax highlighting, you have several options such as
`MarkdownEditing <http://ttscoff.github.io/MarkdownEditing/>`_, `Smart
Markdown <https://github.com/demon386/SmartMarkdown>`_, and `Restructured​Text
Improved <https://bitbucket.org/klorenz/sublimerestructuredtextimproved>`_.
For previewing, you can take the `Markdown Preview
<https://github.com/revolunet /sublimetext-markdown-preview>`_ or a more
powerful previewer supporting multiple markup languages named
`OmniMarkupPreviewer <https://github.com/timonwong/OmniMarkupPreviewer>`_. The
latter is what I actually preferred.


Flexibility
-------------

* `Side​Bar​Enhancements
  <https://sublime.wbond.net/packages/SideBarEnhancements>`_: This plugin
  enhances your sidebar as standard IDE. Common options include create new
  files, open files, move, delete etc.

* `TrailingSpaces <https://sublime.wbond.net/packages/TrailingSpaces>`_:
  Highlighting trailing spaces helps you for code formating, sometimes useful
  in code debugging (e.g., python indent).

* `DocBlockr <https://sublime.wbond.net/packages/DocBlockr>`_: The DocBlockr
  package provides creation and code completion of comment blocks that is
  similar to the default behavior found in other IDEs. It is necessary in
  Sublime Text if only to provide the expected completion behavior when
  opening comment blocks with "/\*\*".

* `SublimeLinter <https://sublime.wbond.net/packages/SublimeLinter>`_: A
  framework for interactive code linting in the Sublime Text 3 editor. Useful
  linters of specific programming languages are not part of SublimeLinter 3
  framework and installed separately. The user can search "Package Control"
  with prefix "SublimeLinter-xxxx" where "xxxx" is specific language lint,
  such as "`SublimeLinter-jshint <https://sublime.wbond.net/packages
  /SublimeLinter-jshint>`_" for JavaScript.

* `Sublime Wrap Plus <https://github.com/ehuss/Sublime-Wrap-Plus>`_: Enhanced
  "wrap lines" command for Sublime Text 2 or 3. This is for the manual hard
  line wrap command (Alt-Q in Windows, Command-Alt-Q in OS X). It does not
  affect the automatic soft line wrapping. It handles a variety of lists, like
  bulleted lists or numbered lists. Lines with subsequent indents should
  maintain their indent. In a source code file, it transparently handles
  single-line comment characters. Lines with email-style quoting are also
  handled.

* `Clickable URL <https://github.com/leonid-
  shevtsov/ClickableUrls_SublimeText2>`_: A tiny SublimeText plugin that would
  be very useful when you find a bunch of URLs within your codes. Basically,
  it will make the URLs clickable.

Handy tricks
---------------------

* Text manipulation tricks: `<http://sublimetexttips.com/7-handy-text-
  manipulation-tricks-sublime-text-2/>`_
* 12 Most-Wanted Sublime Text Tips and Tricks: `<http://www.hongkiat.com/blog
  /sublime-text-tips/>`_