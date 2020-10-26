============
Installation
============

Support
    - **OS Support**: Linux, Windows, Mac
    - **Language Support**: Python 2.x, 3.x

Option 1: installing through `pip <https://pypi.org/project/Filezen/>`__ (Recommended)
======================================================================================

`pypi package link <https://pypi.org/project/Filezen/>`__

``$ pip install Filezen``

If you are behind a proxy

``$ pip --proxy [username:password@]domain_name:port install Filezen``

**Note:** If you get ``command not found`` then
``$ sudo apt-get install python-pip`` should fix that

Option 2: Installing from source (Only if you must)
===================================================

.. code:: bash

    $ git clone https://github.com/ab-anand/Filezen.git
    $ cd Filezen/
    $ pip install -r requirements.txt
    $ python setup.py install

**Note:** If you get ``permission denied`` then
``$ sudo python setup.py install`` should fix that
