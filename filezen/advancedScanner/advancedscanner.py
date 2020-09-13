#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
NOTE ON ADVANCEDSCANNER
=====================

* This program uses the FREQUENCYHEAP to
maintain the most used folder location to store
files of a particular type.

* Using the heap built, it move the files to the
corresponding directory.

* If a file with the same name is already present in
that mapping directory, then the file won't be moved.

"""


import os
import shutil
import json

from pathlib import Path
from collections import defaultdict
from filezen.frequencyHeap import frequencyheap


class AdvancedScanner:
    """
    This class maintains a dictionary with
    key being the file type and value being a
    FREQUENCYHEAP. It then move the files according
    to this dictionary.
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
    def __isValidDir(path):
        """
        checks whether the given path
        exists in the directory or not

        :type path: string
        :param path: the path to check
        :return: 1 if path exists, 0 if it doesn't
        """

        return os.path.isdir(path)

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
    def __getFileExtension(file):
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
    def __readRootFiles(inputPath):
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
    def __readAddressRecursively(outputPath, depth):
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
        for file in targetAddresses:
            fileExtension = self.__getFileExtension(file)
            fileAddress = os.path.dirname(file)
            self.extensionsDict[fileExtension].appendAddress(fileAddress)

    @staticmethod
    def __checkAndMove(sourceFile, destination):
        try:
            _ = shutil.move(sourceFile, destination, copy_function=shutil.copytree)
            return 1
        except shutil.Error:
            return 0
            # print("{}. File NOT moved.".format(str(e)))

    def __moveFilesToTargetFolders(self, rootFiles):
        status = {"Moved": [], "NotMoved": []}
        
        # iterate in rootFiles
        for file in rootFiles:
            fileExtension = self.__getFileExtension(file)
            destinationsList = self.extensionsDict[fileExtension].getValueList

            # check if the file ever occurred in the destination path
            if len(destinationsList) == 0:
                destination = self.outputPath
            else:
                destination = self.extensionsDict[fileExtension].getMaxOccurringAddress

            # print("Moving '{}' to '{}' folder.".format(os.path.basename(file), destination))
            isMoved = self.__checkAndMove(file, destination)

            if isMoved:
                status["Moved"].append(os.path.basename(file))
            else:
                status["NotMoved"].append(os.path.basename(file))

        return status

    def readDirectory(self, inputPath, depth=5, outputPath=None):
        """
        :type outputPath: string
        :type depth: integer
        :type inputPath: string
        """

        errorInputPath = "The specified input directory doesn't exist."
        errorOutputPath = "The specified output directory doesn't exist."
        errorDepth = "Depth cannot be less than 0."

        assert self.__isValidDir(inputPath), errorInputPath
        assert self.__isValidDepth(depth), errorDepth
        if outputPath is not None:
            assert self.__isValidDir(outputPath), errorOutputPath

        self.inputPath = inputPath
        self.depth = depth
        if (self.outputPath is None) and (outputPath is None):
            self.outputPath = inputPath
        elif outputPath is not None:
            self.outputPath = outputPath

        # print(self.inputPath, inputPath, outputPath)

        #  read input files
        rootFiles = self.__readRootFiles(self.inputPath)
        # print(rootFiles)

        #  read target addresses
        targetAddresses = self.__readAddressRecursively(self.outputPath, self.depth)
        # print(targetAddresses)

        #  form extensions dict from target address list
        self.__fillExtensionsDict(targetAddresses)
        # print(self.extensionsDict[".json"].getMaxOccurringAddress)

        # move files to targets
        transferStatusDict = self.__moveFilesToTargetFolders(rootFiles)
        return json.dumps(transferStatusDict, indent=4)

    def setOutputPath(self, outputPath):
        """
        set the depth of scanning

        :type outputPath: string
        :param outputPath: the output folder where the files needs to be moved
        """

        error = "The specified output directory doesn't exist."
        assert self.__isValidDir(outputPath), error
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
