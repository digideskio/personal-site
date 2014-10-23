Python grammer and coding style checking tools
##############################################
:date: 2014-04-26 17:06
:author: caesar0301
:category: Programming
:tags: flake8, pep8, Python

In this post, several python/C coding style documentaion and static chekcing
tools are introduced.

**Style recommendations**:

The main proposals in python ecosystem is indexed by PEPs (Python Enhancement
Proposals)_ whose index number is allocated by the PEP editors.  In PEPs, the
7th (PEP7_) and 8th (PEP8_) proposals defines the C and Python coding
styles recommended.

Another important feature in Python is a clear and readable in-code
documentation, also called "docstring" in python. `PEP257`_ shows a simple
recommendation about that.

**Static checking tools**:

Brilliant pythoners have contributed several wonderful grammer/style analyzing
tools in accordance with PPE8 recommendation, such as `flake8`_, `pep8
(package)`_, `PyChecker`_, `PyFlakes`_, `PyLint`_ etc. For my faviorate, flake8
meets most of my requirements in daily programming. But you can choose a
suitable one for yourself. For others' opinions, you can follow the thread on
`StackOverflow`_.

**Editor plugins**:

For Sublime Text, flake8 has its plugin `Flake8Lint`_. You can also ask google
about your package option. In eclipse, pep8 is integrated in PyDev (2.3.0+) by
default. You can enable it manully if its not activated in your settings:

Open Window > Preferences > PyDev > Editor > Code Analysis > pep8.py



.. _PEPs (Python Enhancement Proposals): http://legacy.python.org/dev/peps/
.. _PEP7: http://legacy.python.org/dev/peps/pep-0007/
.. _PEP8: http://legacy.python.org/dev/peps/pep-0008/
.. _PEP257: http://legacy.python.org/dev/peps/pep-0257/
.. _flake8: https://pypi.python.org/pypi/flake8
.. _pep8 (package): https://pypi.python.org/pypi/pep8
.. _PyChecker: http://pychecker.sourceforge.net/
.. _PyFlakes: https://pypi.python.org/pypi/pyflakes
.. _PyLint: http://www.pylint.org/
.. _StackOverflow: http://stackoverflow.com/q/35470/1320284
.. _Flake8Lint: https://github.com/dreadatour/Flake8Lint
