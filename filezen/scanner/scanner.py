#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
NOTE ON SCANNER
=====================

* This program contains some
generic functions like directory
validation, getting file extension, etc.

"""

import os
import shutil

from pathlib import Path


class Scanner:
    """
    This class is used as a
    parent/super class for Simple
    & Advanced Scanners
    """

    @staticmethod
    def isValidDir(path):
        """
        checks whether the given path
        exists in the directory or not

        :type path: string
        :param path: the path to check
        :return: 1 if path exists, 0 if it doesn't
        """

        return os.path.isdir(path)

    @staticmethod
    def getFileExtension(file):
        """
        finds the file extension

        :type file: string
        :param file: the file whose extension is needed
        :return: extension of the file
        """

        extension = Path(file).suffix
        if extension == '':
            extension = os.path.basename(file)

        return extension

    @staticmethod
    def readRootFiles(inputPath):
        """
        read files present in the inputPath
        which are needed to be organized/moved

        :type inputPath: string
        :param inputPath: the input folder where the cluttered files reside
        :return: list of files present in inputPath
        """

        files = []
        for (_, _, filenames) in os.walk(inputPath):
            files.extend(filenames)
            break

        files = [os.path.join(inputPath, file) for file in files]

        return files

    @staticmethod
    def checkAndMove(sourceFile, destination):
        """
        checks if a file with same name is
        already present in a folder, if not then
        moves the sourceFile to destination

        :type sourceFile: string
        :param sourceFile: absolute path of file to move
        :type destination: string
        :param destination: absolute path of the destination
        :return: 1 if file is moved properly, 0 if a same file name is already present
        """

        try:
            _ = shutil.move(sourceFile, destination, copy_function=shutil.copytree)
            return 1
        except shutil.Error:
            return 0
