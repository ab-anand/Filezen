import unittest
import sys


from filezen.frequencyHeap import frequencyheap

sys.path.insert(0, '..')


class TestFrequencyHeap(unittest.TestCase):

    def setUp(self):
        self.heap = frequencyheap.MaxFrequency()
        self.heap.appendAddress("home/Documents/")
        self.heap.appendAddress("home/Documents/")
        self.heap.appendAddress("home/Downloads/")

    def test_appendAddress(self):
        self.heap.appendAddress("home/Documents/")
        self.heap.appendAddress("home/Documents/")
        self.heap.appendAddress("home/Downloads/")
        result = len(self.heap.getValueList)
        correct_answer = 6
        self.assertEqual(result, correct_answer)

    def test_getMaxOccurringAddress(self):
        result = self.heap.getMaxOccurringAddress
        correct_answer = "home/Documents/"
        self.assertEqual(result, correct_answer)

    def test_getValueList(self):
        result = self.heap.getValueList
        correct_answer = ["home/Documents/", "home/Documents/", "home/Downloads/"]
        self.assertEqual(result, correct_answer)


if __name__ == '__main__':
    unittest.main()
