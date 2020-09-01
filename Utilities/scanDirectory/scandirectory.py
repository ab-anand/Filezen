import os
import shutil
from pathlib import Path

from collections import defaultdict
from Utilities.frequencyHeap import frequencyheap


class Scanner:
    def __init__(self):
        self.inputPath = None
        self.depth = 5
        self.outputPath = None
        self.extensionsDict = defaultdict(frequencyheap.MaxFrequency)

    @staticmethod
    def __isValidDir(path):
        return os.path.isdir(path)

    @staticmethod
    def __getFileExtension(file):
        extension = Path(file).suffix
        if extension == '':
            extension = os.path.basename(file)

        return extension

    @staticmethod
    def __readRootFiles(inputPath):
        files = []
        for (_, _, filenames) in os.walk(inputPath):
            files.extend(filenames)
            break

        return files

    @staticmethod
    def __readAddressRecursively(outputPath, depth):
        fileSeparator = os.sep
        baseDepth = len(outputPath.split(fileSeparator))
        filesList = [(root, dirs, files) for root, dirs, files, in os.walk(outputPath)]
        allFiles = []
        for file in filesList:
            fileDepth = len(file[0].split(fileSeparator))
            if fileDepth - baseDepth > depth:
                continue
            allFiles.append(file)

        return allFiles

    def __fillExtensionsDict(self, targetAddresses):
        for file in targetAddresses:
            fileExtension = self.__getFileExtension(file)
            fileAddress = os.path.dirname(file)
            self.extensionsDict[fileExtension].appendAddress(fileAddress)

    @staticmethod
    def __checkAndMove(sourceFile, destination):
        try:
            dest = shutil.move(sourceFile, destination, copy_function=shutil.copytree)
        except shutil.Error as e:
            print("{}. File NOT moved.".format(str(e)))

    def __moveFilesToTargetFolders(self, rootFiles):
        # iterate in rootFiles
        for file in rootFiles:
            fileExtension = self.__getFileExtension(file)
            destinationsList = self.extensionsDict[fileExtension].getValueList
            # check if the file ever occurred in the destination path
            if len(destinationsList) == 0:
                destination = self.outputPath
            else:
                destination = self.extensionsDict[fileExtension].getMaxOccurringAddress

            print("Moving '{}' to '{}' folder.".format(os.path.basename(file), destination))
            self.__checkAndMove(file, destination)

    def readDirectory(self, inputPath, depth=5, outputPath=None):
        """
        :type outputPath: string
        :type depth: integer
        :type inputPath: string
        """

        self.inputPath = inputPath
        self.depth = depth
        if outputPath is None:
            self.outputPath = inputPath
        else:
            self.outputPath = outputPath

        if not self.__isValidDir(inputPath):
            print("Input Directory invalid")
        if not self.__isValidDir(outputPath):
            print("Output Directory invalid")

        #  read input files
        rootFiles = self.__readRootFiles(self.inputPath)

        #  read target addresses
        targetAddresses = self.__readAddressRecursively(self.outputPath, self.depth)

        #  form extensions dict from target address list
        self.__fillExtensionsDict(targetAddresses)

        # move files to targets
        self.__moveFilesToTargetFolders(rootFiles)

    def setOutputPath(self, outputPath):
        if self.__isValidDir(outputPath):
            self.outputPath = outputPath
        else:
            pass
