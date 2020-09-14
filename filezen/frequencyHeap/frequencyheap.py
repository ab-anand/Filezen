#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
NOTE ON FREQUENCYHEAP
===================== \
* This program will maintain a heap of file
locations according to their occurrences. \
* It helps to get the folder location where a
file of a particular type is stored. \
"""

from collections import Counter


class MaxFrequency:
    """Defined class builds a heap
    of elements according to their occurrence
    """

    def __init__(self):
        """initializes the heap of file locations"""
        self.folderAddresses = []

    def appendAddress(self, path):
        """adds new addresses to the heap

        :type path: string
        :param path: the file path to add to the heap
        """

        self.folderAddresses.append(path)

    @property
    def getMaxOccurringAddress(self):
        """returns the most occurring folder location in the heap

        :return: most frequent folder location: string
        """

        folderAddress = Counter(self.folderAddresses).most_common(1)
        return folderAddress[0][0]

    @property
    def getValueList(self):
        """returns the complete heap

        :return: the heap of folder locations
        """

        return self.folderAddresses
