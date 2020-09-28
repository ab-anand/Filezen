.. figure:: https://i.imgur.com/opeYy4q.jpg
    :figclass: align-center
    :alt:

Filezen
=======

|version| |readthedocs.org| |codecov| |build| |pypi| |license| |deepsource| |coffee|


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
- Minimum dependencies ( just uses ``Pathlib`` if only you're working with Python 2.x )
- Easy to use
- Fast!
- Returns ``JSON`` objects
- Support
    - **OS Support**: Linux, Windows, Mac
    - **Language Support**: Python 2.x, 3.x

Installation
------------
`[back to top] <https://github.com/ab-anand/Filezen#filezen>`__

Option 1: installing through `pip <https://pypi.org/project/Filezen/>`__ (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`pypi package link <https://pypi.org/project/Filezen/>`__

``$ pip install Filezen``

If you are behind a proxy

``$ pip --proxy [username:password@]domain_name:port install Filezen``

**Note:** If you get ``command not found`` then
``$ sudo apt-get install python-pip`` should fix that

Option 2: Installing from source (Only if you must)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ git clone https://github.com/ab-anand/Filezen.git
    $ cd Filezen/
    $ pip install -r requirements.txt
    $ python setup.py install

**Note:** If you get ``permission denied`` then
``$ sudo python setup.py install`` should fix that


Usage
-----
`[back to top] <https://github.com/ab-anand/Filezen#filezen>`__

Simple Scanner
~~~~~~~~~~~~~~
.. figure:: https://i.imgur.com/KEOFHQn.gif
   :alt:

- ``Simple Scanner`` uses a predefined `mapping <https://github.com/ab-anand/Filezen/blob/master/filezen/simpleScanner/extensionMapper.py/>`__ of filetypes to folder ``e.g. ".csv": "Documents"``.
- Based on this mapping it creates directories(only if they don't exist already) and organizes files into them as shown in the above Fig.
- Using ``Simple Scanner``

.. code:: python

    >>> from filezen import SimpleScanner as scanner
    >>> input_directory = "/home/abhinav/Downloads"
    >>> output_directory = "/home/abhinav/Documents"
    >>> result = scanner.cleanDirectory(input_directory, outputPath=output_directory)
    >>> print(result)
    '{
        "Moved": [
            "FileA.pdf",
            "FileB.txt",
            "FileC.mp4",
            "FileD.log",
            "FileB.xyz"
        ],
        "NotMoved": [

        ]
    }'

- If no **Output Directory** is specified, then ``Simple Scanner`` would treat **Input Directory** as the **Output Directory**  thus creating folders in the **Input Directory** itself.

Advanced Scanner
~~~~~~~~~~~~~~~~
.. figure:: https://i.imgur.com/L2aARhU.gif
   :alt:

- ``Advanced Scanner`` maintains a ``heap`` for each filetype/file-extension it encounters while scanning the **Output Directory**.
- This ``heap`` contains all the directory addresses where a particular filetype(``e.g. "pdf"``) occurs.
- The address having the highest number of occurrence of that filetype is at the **top** of the ``heap``
- With the help of this heap it finally decides the directory where a particular filetype has mostly occurred and thus moving the all such files into that directory.
- As shown in the above image, ``Advanced Scanner`` scans the ``child`` as well as ``sibling directories`` (at the same level).
- The level of child directories to scan is decided by ``depth`` parameter as shown in the example below.
- By default, ``depth = 5``
- Using ``Advanced Scanner``

.. code:: python

    >>> from filezen import AdvancedScanner as scanner
    >>> input_directory = "/home/abhinav/Downloads"
    >>> output_directory = "/home/abhinav/Documents"
    >>> depth = 3
    >>> result = scanner.cleanDirectory(input_directory, outputPath=output_directory, depth=depth)
    >>> print(result)
    '{
        "Moved": [
            "FileA.pdf",
            "FileB.txt",
            "FileC.mp4",
            "FileD.log",
            "FileE.xyz"
        ],
        "NotMoved": [

        ]
    }'

- If no **Output Directory** is specified, then ``Advanced Scanner`` would read the folders in the **Input Directory** itself and move accordingly.

**Note:** If a file with the same name is already present in the **Output Directory** then ``Filezen`` would
ignore the file and leave it to the user. In the resulting JSON, you'll get the all such filenames which
were not moved in the ``NotMoved`` list.


Applications
~~~~~~~~~~~~

- `KRETA  <https://github.com/ab-anand/Kreta/>`__ - It is a command line application which uses ``Filezen`` to organize file.

.. figure:: https://i.imgur.com/PPiTMY6.gif
    :alt:

- `Watch Simple Scanner in action with Kreta <https://github.com/ab-anand/Filezen/blob/master/SIMPLESCANNER.rst>`__.
- `Watch Advanced Scanner in action with Kreta <https://github.com/ab-anand/Filezen/blob/master/ADVANCEDSCANNER.rst>`__.


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

You can find a copy of the License at `http://abhinav.mit-license.org/ <http://abhinav.mit-license.org/>`__


|producthunt|

.. |readthedocs.org| image:: https://readthedocs.org/projects/filezen/badge/?version=latest
   :target: https://filezen.readthedocs.io/en/latest/index.html
.. |license| image:: https://img.shields.io/github/license/ab-anand/FileZen?color=red
   :target: https://github.com/ab-anand/FileZen/blob/master/LICENSE
.. |build| image:: https://travis-ci.com/ab-anand/Filezen.svg?branch=master
   :target: https://github.com/ab-anand/FileZen
.. |pypi| image:: https://img.shields.io/pypi/pyversions/Filezen
    :target: https://pypi.org/project/Filezen/
.. |version| image:: https://img.shields.io/pypi/v/Filezen?color=orange
    :target: https://pypi.org/project/Filezen/
.. |codecov| image:: https://codecov.io/gh/ab-anand/Filezen/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/ab-anand/Filezen
.. |deepsource| image:: https://deepsource.io/gh/ab-anand/Filezen.svg/?label=active+issues&show_trend=true)](https://deepsource.io/gh/ab-anand/Filezen/?ref=repository-badge
    :target: https://github.com/ab-anand/FileZen
.. |producthunt| image:: https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=267022&theme=dark
    :target: https://www.producthunt.com/posts/filezen
    :scale: 10 %
.. |coffee| image:: https://i.imgur.com/qeNEiac.png?1
    :target: https://www.buymeacoffee.com/abhiinav
