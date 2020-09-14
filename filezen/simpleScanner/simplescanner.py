#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
NOTE ON SIMPLESCANNER
=====================

* This program uses a predefined mapping
to store a particular file type from the
input directory.

* Validates the folder location and moves a file
according to the mapping.

* If a file with the same name is already present in
that mapping directory, then the file won't be moved.

"""


import os
import json

from filezen.simpleScanner.extensionMapper import extensionsToFolder
from filezen.scanner import scanner


class SimpleScanner(scanner.Scanner):
    """
    This class moves the input files
    using a predefined mapping. Inherits
    some methods from Scanner.
    """

    def __init__(self):
        self.extensionsToFolder = extensionsToFolder
        self.inputPath = None
        self.outputPath = None

    def __moveFilesToTargetFolders(self, rootFiles):
        """
        iteratively goes through each file
        in the input directory and using the
        extensionsDict it finds the location
        for a file type then using checkAndMove
        function it moves the files

        :type rootFiles: list
        :param rootFiles: list of files in the input folder
        :return: a dictionary with list of files that were moved/not-moved
        """

        status = {"Moved": [], "NotMoved": []}

        # iterate in rootFiles
        for file in rootFiles:
            fileExtension = self.getFileExtension(file)

            if fileExtension in extensionsToFolder:
                folderType = extensionsToFolder[fileExtension]
            else:
                folderType = extensionsToFolder["default"]

            completeFolderPath = os.path.join(self.outputPath, folderType)

            if not os.path.exists(completeFolderPath):
                os.makedirs(completeFolderPath)

            isMoved = self.checkAndMove(file, completeFolderPath)
            if isMoved:
                status["Moved"].append(os.path.basename(file))
            else:
                status["NotMoved"].append(os.path.basename(file))

        return status

    def readDirectory(self, inputPath, outputPath=None):
        """
        The main functions which takes inputPath &
        outputPath and validates them. Then
        calling the required functions in order to move
        the files to their respective locations

        :type outputPath: string
        :param outputPath: absolute path of the folder containing output files
        :param inputPath: absolute path of the folder containing input files
        :type inputPath: string
        :return: json containing list of file that were moved/not-moved
        """

        errorInputPath = "The specified input directory doesn't exist."
        errorOutputPath = "The specified output directory doesn't exist."

        assert self.isValidDir(inputPath), errorInputPath
        if outputPath is not None:
            assert self.isValidDir(outputPath), errorOutputPath

        self.inputPath = inputPath
        if (self.outputPath is None) and (outputPath is None):
            self.outputPath = inputPath
        elif outputPath is not None:
            self.outputPath = outputPath

        #  read input files
        rootFiles = self.readRootFiles(self.inputPath)

        # move files to targets
        transferStatusDict = self.__moveFilesToTargetFolders(rootFiles)

        return json.dumps(transferStatusDict, indent=4)

    def setOutputPath(self, outputPath):
        """
        set the output folder

        :type outputPath: string
        :param outputPath: the output folder where the files needs to be moved
        """

        error = "The specified output directory doesn't exist."
        assert self.isValidDir(outputPath), error
        self.outputPath = outputPath
