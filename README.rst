******************
django-closuretree
******************


.. image:: https://travis-ci.com/sam-mi/django-closuretree.svg?branch=master
   :target: https://travis-ci.com/sam-mi/django-closuretree
   :alt: Build Status
.. image:: https://coveralls.io/repos/github/sam-mi/django-closuretree/badge.svg?branch=master
   :target: https://coveralls.io/github/sam-mi/django-closuretree?branch=master
   :alt: Test Coverage

``django-closuretree`` is an implementation of the `closure tree <http://homepages.inf.ed.ac.uk/libkin/papers/tc-sql.pdf>`_ technique for `Django <https://djangoproject.com>`_ applications designed to provide efficient querying of `tree-based structures <http://en.wikipedia.org/wiki/Tree_%28data_structure%29>`_ in a relational database. Its goal is to reduce the number of queries required when querying the children or parents of a given object.

This is a folk of `the original work by Ocado Technology<https://github.com/ocadotechnology/django-closuretree>`_ with a few extra features from fork https://github.com/ykiu/django-closuretree.

Given the following model:

.. code-block:: python

    class Node(models.Model):
        name = models.CharField(max_length=24)
        parent = models.ForeignKey('self', related_name='children')

The children of each model can be queried with:

.. code-block:: python

    Node.objects.get(name='A').children.all()

However, for recursive lookups, this results in a large number of queries. Instead, ``django-closuretree`` allows you to extract them all in one go:

.. code-block:: python

    from closuretree.models import ClosureModel

    class Node(ClosureModel):
        name = models.CharField(max_length=24)
        parent = models.ForeignKey('self', related_name='children', null=True)

    a = Node.objects.create(name='A')
    Node.objects.create(name='B', parent=a)

    Node.objects.get(name='A').get_descendants()

A single query will obtain all the descendants.

===========
Quick Start
===========

* Install ``django-closuretree`` with ``pip install git+https://github.com/sam-mi/django-closuretree.git``.
* Inherit your models from ``closuretree.models.ClosureModel`` instead of ``django.db.models.Model``.

That's it. You can now use ``get_descendants()`` and ``get_ancestors()`` on a model instance.

If you're adding this to an existing application that already has data in the database, you'll need to run the ``rebuildtable()`` method of each model before the closure tree will be populated with the existing data:

.. code-block:: python

    Node.rebuildtable()

============
Contributing
============

1. Fork the repo and create your branch from master.
2. Do your work.
3. Run tests (``setup.py test``). Dependencies will be installed into `./.eggs/`. No need to explicitly activate a virtual environment.
4. Make a PR.

We ask that contributors adhere to `PEP8 <https://www.python.org/dev/peps/pep-0008/>`_ standards, and include full tests for all their code.
