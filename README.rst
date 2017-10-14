find-redirects
==============

Find URLs that lead to 301 or 302 redirects in the specified set of
files. Optionally, update the redirected URLs in-place to their targets
URLs.

Installation
------------

If you're on `a snap enabled system <https://snapcraft.io>`__:

.. code:: bash

    sudo snap install find-redirects

Otherwise, you can install with Pip:

.. code:: bash

    sudo pip3 install find-redirects

Usage
-----

There are a number of ways to use ``find-redirects``. You can see all
the options by typing ``find-redirects --help``.

Find URLs that have moved
~~~~~~~~~~~~~~~~~~~~~~~~~

At it's simplest, ``find-redirects`` will tell you which URLs have moved
in a set of files:

.. code:: bash

    $ find-redirects index.html about.html
    Found 2 URLs in 2 files
    Found redirect: https://example.com/place1 - https://example.com/place/one
    Found redirect: https://example.com/place2 - https://example.com/place/two

``find-redirects`` can understand any Glob expression for finding files,
so in the above example, ``index.html about.html`` could have been
replaced with ``*.html`` or ``**/*.html``.

Update URLs that have moved in files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``find-redirects`` can also update file in-place. (To be on the safe
side you should ideally make sure your files are stored in version
control, e.g. Git, before updating files in-place):

.. code:: bash

    $ find-redirects --replace index.html about.html
    Found 2 URLs in 2 files
    Found redirect: http://127.0.0.1:5000/place1 - http://127.0.0.1:5000/place/one
    Found redirect: http://127.0.0.1:5000/place2 - http://127.0.0.1:5000/place/two
    Updating index.html
    Updating about.html
    Replaced 2 URLs in 2 files

Error if redirects are found
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You may wish to throw an error if *any* redirects are found. This might
be useful for example in CI systems. To achieve this, use ``--strict``
mode:

.. code:: bash

    $ find-redirects --strict index.html about.html || echo "**Failed**"
    Found 2 URLs in 2 files
    Found redirect: https://example.com/place1 - https://example.com/place/one
    Found redirect: https://example.com/place2 - https://example.com/place/two
    **Failed**
