from collections import Counter


class MaxFrequency:
    def __init__(self):
        self.folderAddresses = []

    def appendAddress(self, path=None):
        self.folderAddresses.append(path)

    @property
    def getMaxOccurringAddress(self):
        folderAddress = Counter(self.folderAddresses).most_common(1)
        return folderAddress[0][0]

    @property
    def getValueList(self):
        return self.folderAddresses
