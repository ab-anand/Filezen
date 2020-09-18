.. figure:: https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQw8G45wF_X-W_IA4Uce47WPIScVd3Ixpj0UA&usqp=CAU
   :alt:

Filezen
=======

|readthedocs.org| |license| |build|

*An Intelligent file organizer module which reads your file storing pattern & move
the cluttered files accordingly!*

:Author: Abhinav Anand

.. contents::
    :backlinks: none

.. sectnum::

What is it
---------------
`[back to top] <https://github.com/ab-anand/Filezen#filezen>`__

*Let's accept, no one likes to organize files on a regular basis. Even if you do, you
wouldn't want to do it everytime you download a new file.*

Guess what! Filezen got you covered.

Given a folder of your cluttered/unorganized files, using ``Filezen``, you can achieve
the following

- If you've never maintained specific directories for your files. Then ``Filezen's Basic Scanner`` can create suitable folders and organize your file into them.

- If you already have a pattern of directories for storing different files. Then ``Filezen's Advanced Scanner`` can read your file storing pattern and move your files accordingly.

Features
--------
`[back to top] <https://github.com/ab-anand/Filezen#filezen>`__

- **Advanced Scanning**
- **Basic Scanning**
- Minimum dependencies(just uses ``Pathlib`` if only you're working with Python 2.x)
- Easy to use
- Fast!
- Support
    - **OS Support**: Linux, Windows, Mac
    - **Language Support**: Python 2.x, 3.x

Installation
------------
`[back to top] <https://github.com/ab-anand/Filezen#filezen>`__

Option 1: installing through `pip <https://test.pypi.org/project/Filezen>`__ (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`pypi package link <https://test.pypi.org/project/Filezen>`__

``$ pip install -i https://test.pypi.org/simple/ Filezen``

If you are behind a proxy

``$ pip --proxy [username:password@]domain_name:port install -i https://test.pypi.org/simple/ Filezen``

**Note:** If you get ``command not found`` then
``$ sudo apt-get install python-pip`` should fix that

Option 2: Installing from source (Only if you must)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ git clone https://github.com/ab-anand/Filezen.git
    $ cd Filezen/
    $ pip install -r requirements.txt
    $ python setup.py install

Usage
-----


Documentation
-------------
`[back to top] <https://github.com/ab-anand/Filezen#filezen>`__

For a detailed usage example, refer the `documentation at Read the Docs <https://filezen.readthedocs.io/en/latest/>`__


Contributing
------------
`[back to top] <https://github.com/ab-anand/Filezen#filezen>`__

Please refer `Contributing page for details <https://github.com/ab-anand/Filezen/blob/master/CONTRIBUTING.rst>`__


Bugs
----
`[back to top] <https://github.com/ab-anand/Filezen#filezen>`__

Please report the bugs at the `issue
tracker <https://github.com/ab-anand/Filezen/issues>`__



License
-------
`[back to top] <https://github.com/ab-anand/Filezen#filezen>`__


Built with ♥ by `Abhinav Anand <https://github.com/ab-anand/>`__ under the `MIT License <https://github.com/ab-anand/Filezen/blob/master/LICENSE/>`__ ©




.. |readthedocs.org| image:: https://readthedocs.org/projects/filezen/badge/?version=latest
   :target: https://filezen.readthedocs.io/en/latest/index.html
.. |license| image:: https://img.shields.io/github/license/ab-anand/FileZen?color=red
   :target: https://github.com/ab-anand/FileZen/blob/master/LICENSE
.. |build| image:: https://travis-ci.com/ab-anand/Filezen.svg?branch=master
   :target: https://github.com/ab-anand/FileZen


