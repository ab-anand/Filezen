import unittest
import sys
import os
import shutil
from filezen.scanner import scanner

sys.path.insert(0, '..')


class TestScanner(unittest.TestCase):
    def setUp(self):
        self.scanner = scanner.Scanner()
        cwd = os.getcwd()
        test_directory = "scantest"
        path = os.path.join(cwd, test_directory)
        if not os.path.exists(path):
            os.mkdir(path)
        self.test_dir_path = path

    def test_isValidDir(self):
        result = self.scanner.isValidDir('/bin')
        self.assertEqual(True, result)

    def test_getFileExtension(self):
        result_1 = self.scanner.getFileExtension("test.pdf")
        correct_answer_1 = ".pdf"
        self.assertEqual(correct_answer_1, result_1)

        result_2 = self.scanner.getFileExtension("Dockerfile")
        correct_answer_2 = "Dockerfile"
        self.assertEqual(result_2, correct_answer_2)

    def test_readRootFiles(self):
        cwd = os.path.join(os.getcwd(), "tests")
        result = self.scanner.readRootFiles(cwd)
        answer = ["test_simpleScanner.py", "test_scanner.py", "__init__.py",
                  "test_advancedScanner.py", "test_frequencyHeap.py"]
        answer = [os.path.join(cwd, file) for file in answer]

        # avoid pyc files for python 2.7
        correct_result = []
        for res in result:
            if not res.endswith("pyc"):
                correct_result.append(res)

        self.assertEqual(sorted(answer), sorted(correct_result))

    def test_checkAndMove(self):
        test_file = "scannerTestFile.txt"
        with open(test_file, 'w') as fp:
            pass

        result_1 = self.scanner.checkAndMove(test_file, self.test_dir_path)
        correct_answer_1 = True
        self.assertEqual(result_1, correct_answer_1)

        result_2 = self.scanner.checkAndMove(test_file, self.test_dir_path)
        correct_answer_2 = False
        self.assertEqual(result_2, correct_answer_2)

    def tearDown(self):
        shutil.rmtree(self.test_dir_path, ignore_errors=True)


if __name__ == '__main__':
    unittest.main()
