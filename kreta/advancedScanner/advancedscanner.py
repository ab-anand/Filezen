import os
import shutil

from pathlib import Path
from collections import defaultdict
from kreta.frequencyHeap import frequencyheap


class AdvancedScanner:
    def __init__(self):
        self.inputPath = None
        self.depth = 5
        self.outputPath = None
        self.extensionsDict = defaultdict(frequencyheap.MaxFrequency)

    @staticmethod
    def __isValidDir(path):
        return os.path.isdir(path)

    @staticmethod
    def __isValidDepth(depth):
        return depth >= 0

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
        return transferStatusDict

    def setOutputPath(self, outputPath):
        error = "The specified output directory doesn't exist."
        assert self.__isValidDir(outputPath), error
        self.outputPath = outputPath

    def setDepth(self, depth):
        error = "Depth cannot be less than 0."
        assert self.__isValidDepth(depth), error
        self.depth = depth
