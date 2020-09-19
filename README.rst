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
`[back to top] <https://github.com/ab-anand/Filezen#filezen>`__

Simple Scanner
~~~~~~~~~~~~~~
.. figure:: https://i.imgur.com/KEOFHQn.gif
   :alt:

- ``Simple Scanner`` uses a predefined `mapping <https://github.com/ab-anand/Filezen/blob/master/filezen/simpleScanner/extensionMapper.py/>`__ of filetypes to folder.
- Based on this mapping it creates directories and organizes files into them as shown in the above Fig.
- Using ``Simple Scanner``

.. code:: python

    >>> from filezen.simpleScanner import simplescanner as SSC
    >>> scanner = SSC.SimpleScanner()
    >>> input_directory = "/home/abhinav/Downloads"
    >>> output_directory = "/home/abhinav/Documents"
    >>> result = scanner.readDirectory(input_directory, outputPath=output_directory)
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

- If a file with the same name is already present in the *Output Directory* then ``Simple Scanner`` would ignore the file and leave it to the user.
- The filename which hasn't being because of the reason stated above would be returned in the ``NotMoved`` array of the result.
- If no *Output Directory* is specified, then ``Simple Scanner`` would create folders in the *Input Directory* itself.

Advanced Scanner
~~~~~~~~~~~~~~~~
.. figure:: https://i.imgur.com/L2aARhU.gif
   :alt:

- ``Advanced Scanner`` maintains a ``heap`` for each filetype it encounters while scanning the *Output Directory*.
- With the help of this heap it finally decides the directory where a particular filetype has mostly occurred and thus moving the file into that directory.
- As shown in the above image, ``Advanced Scanner`` scans the child directories also.
- The level of child directories to scan is decided by ``depth`` parameter as shown in the example below.
- By default, ``depth = 5``
- Using ``Advanced Scanner``

.. code:: python

    >>> from filezen.advancedScanner import advancedscanner as ASC
    >>> scanner = ASC.AdvancedScanner()
    >>> input_directory = "/home/abhinav/Downloads"
    >>> output_directory = "/home/abhinav/Documents"
    >>> depth = 3
    >>> result = scanner.readDirectory(input_directory, outputPath=output_directory, depth=depth)
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

- Similar to ``Simple Scanner``, if a file with the same name is already present in the *Output Directory* then ``Advanced Scanner`` would ignore the file and leave it to the user.
- The filename which hasn't being because of the reason stated above would be returned in the ``NotMoved`` array of the result.
- If no *Output Directory* is specified, then ``Advanced Scanner`` would read the folders in the *Input Directory* itself and move accordingly.

Applications
~~~~~~~~~~~~

- KRETA - It is a command line application which uses ``Filezen`` to organize file.


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


