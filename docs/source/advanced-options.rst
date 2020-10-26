================
Advanced Options
================

Simple Scanner
~~~~~~~~~~~~~~


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

