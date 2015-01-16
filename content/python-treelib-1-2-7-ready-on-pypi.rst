Python treelib 1.2.7 ready on PyPi
##################################

:date: 2014-04-26 17:37
:author: caesar0301
:tags: Python, tree

`treelib`_ is an efficient and useful implementation of `tree data
structure`_ in Python. Now its newest version of 1.2.7 is available on
PyPI. You can install it with "sudo easy\_install -U treelib" or find
the latest update on `github`_.

The main features of *treelib* includes:

-  Simple to use in both python 2 and 3.
-  Efficient operation of node indexing with the benefit of dict type.
-  Support various tree operations like traversing, insertion, deletion,
   node moving, shallow/deep copying, subtree cutting etc.
-  Support user-defined data payload to acccelerate your model
   construction.
-  Has pretty tree showing and text/json dump for offline analysis.

For the full API documentation, please visit `treelib API site`_.

Here is a simple example to create a family tree:

::

    tree = Tree()
    tree.create_node("Harry", "harry")  # root node
    tree.create_node("Jane", "jane", parent = "harry")
    tree.create_node("Bill", "bill", parent = "harry")
    tree.create_node("Diane", "diane", parent = "jane")
    tree.create_node("George", "george", parent = "diane")
    tree.create_node("Mary", "mary", parent = "diane")
    tree.create_node("Jill", "jill", parent = "george")
    tree.create_node("Mark", "mark", parent = "jane")
    tree.show()

**Output**:

::

    Harry
    ├── Jane
    │   ├── Mark
    │   └── Diane
    │       ├── Mary
    │       └── George
    │           └── Jill
    └── Bill

.. _treelib: https://github.com/caesar0301/pyTree
.. _tree data structure: http://en.wikipedia.org/wiki/Tree_%28data_structure%29
.. _github: https://github.com/caesar0301/pyTree
.. _treelib API site: http://caesar0301.github.io/pyTree/
