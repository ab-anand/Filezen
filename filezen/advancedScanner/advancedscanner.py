#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
NOTE ON ADVANCEDSCANNER
=======================

* This program uses the FREQUENCYHEAP to
maintain the most used folder location to store
files of a particular type.

* Using the heap built, it move the files to the
corresponding directory.

* If a file with the same name is already present in
that mapping directory, then the file won't be moved.

"""


import os
import json

from collections import defaultdict
from filezen.frequencyHeap import frequencyheap
from filezen.scanner import scanner


class AdvancedScanner(scanner.Scanner):
    """
    This class maintains a dictionary with
    key being the file type and value being a
    FREQUENCYHEAP. It then move the files according
    to this dictionary. Inherits
    some methods from Scanner.
    """

    def __init__(self):
        """
        initializes inputPath,
        depth, outPath & extensionsDict
        required for the class
        """

        self.inputPath = None
        self.depth = 5
        self.outputPath = None
        self.extensionsDict = defaultdict(frequencyheap.MaxFrequency)

    @staticmethod
    def __isValidDepth(depth):
        """
         checks whether the given depth
         is valid or not for our use case

         :type depth: int
         :param depth: the depth to check
         :return: 1 if depth >= 0, 0 otherwise
         """
        return depth >= 0

    @staticmethod
    def __readAddressRecursively(outputPath, depth):
        """
        scans the output folder's file
        storage pattern

        :type outputPath: string
        :param outputPath: the folder to scan
        :type depth: int
        :param depth: levels of folders to scan
        :return: list of absolute path of files in the output folder
        """

        fileSeparator = os.sep
        baseDepth = len(outputPath.split(fileSeparator))
        filesList = [(root, dirs, files) for root, dirs, files, in os.walk(outputPath)]
        allFiles = []
        for file in filesList:
            fileDepth = len(file[0].split(fileSeparator))
            if (fileDepth - baseDepth > depth) or (fileDepth - baseDepth == 0):
                continue
            allFiles.append(file)

        baseFiles = []
        for level in allFiles:
            for file in level[2]:
                file = os.path.join(level[0], file)
                baseFiles.append(file)
        return baseFiles

    def __fillExtensionsDict(self, targetAddresses):
        """
        using the targetAddresses, it fills
        the location heap for types of files present

        :type targetAddresses: list
        :param targetAddresses: the list of files in the output folder
        """

        for file in targetAddresses:
            fileExtension = self.getFileExtension(file)
            fileAddress = os.path.dirname(file)
            self.extensionsDict[fileExtension].appendAddress(fileAddress)

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
            destinationsList = self.extensionsDict[fileExtension].getValueList

            # check if the file ever occurred in the destination path
            if len(destinationsList) == 0:
                destination = self.outputPath
            else:
                destination = self.extensionsDict[fileExtension].getMaxOccurringAddress

            # print("Moving '{}' to '{}' folder.".format(os.path.basename(file), destination))
            isMoved = self.checkAndMove(file, destination)

            if isMoved:
                status["Moved"].append(os.path.basename(file))
            else:
                status["NotMoved"].append(os.path.basename(file))

        return status

    def cleanDirectory(self, inputPath, depth=5, outputPath=None):
        """
        The main functions which takes inputPath,
        outputPath, depth and validates them. Then
        calling the required functions in order to move
        the files to their respective locations

        :type outputPath: string
        :param outputPath: absolute path of the folder containing output files
        :type depth: integer
        :param depth: levels of folders to scan
        :param inputPath: absolute path of the folder containing input files
        :type inputPath: string
        :return: json containing list of file that were moved/not-moved
        """

        errorInputPath = "The specified input directory doesn't exist."
        errorOutputPath = "The specified output directory doesn't exist."
        errorDepth = "Depth cannot be less than 0."

        assert self.isValidDir(inputPath), errorInputPath
        assert self.__isValidDepth(depth), errorDepth
        if outputPath is not None:
            assert self.isValidDir(outputPath), errorOutputPath

        self.inputPath = inputPath
        self.depth = depth
        if (self.outputPath is None) and (outputPath is None):
            self.outputPath = inputPath
        elif outputPath is not None:
            self.outputPath = outputPath

        # print(self.inputPath, inputPath, outputPath)

        #  read input files
        rootFiles = self.readRootFiles(self.inputPath)

        #  read target addresses
        targetAddresses = self.__readAddressRecursively(self.outputPath, self.depth)

        #  form extensions dict from target address list
        self.__fillExtensionsDict(targetAddresses)

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

    def setDepth(self, depth):
        """
        set the depth of scanning

        :type depth: int
        :param depth: the depth up to which scanning would be done
        """

        error = "Depth cannot be less than 0."
        assert self.__isValidDepth(depth), error
        self.depth = depth
