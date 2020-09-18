import unittest
import sys
import os
import shutil
from filezen.simpleScanner import simplescanner

sys.path.insert(0, '..')


class TestSimpleScanner(unittest.TestCase):

    def setUp(self):
        self.simpleScanner = simplescanner.SimpleScanner()
        cwd = os.getcwd()
        test_directory = "scantest"
        path = os.path.join(cwd, test_directory)
        if not os.path.exists(path):
            os.mkdir(path)
        self.test_dir_path = path

    def test_setOutputPath(self):
        self.simpleScanner.setOutputPath(self.test_dir_path)
        result = self.simpleScanner.outputPath

        self.assertEqual(self.test_dir_path, result)

    def tearDown(self):
        shutil.rmtree(self.test_dir_path, ignore_errors=True)


if __name__ == '__main__':
    unittest.main()
