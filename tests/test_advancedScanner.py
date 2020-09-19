import unittest
import os
import sys
import shutil

from filezen.advancedScanner import advancedscanner

sys.path.insert(0, '..')


class TestAdvancedScanner(unittest.TestCase):
    def setUp(self):
        self.advancedscanner = advancedscanner.AdvancedScanner()
        cwd = os.getcwd()
        test_directory = "scantest"
        path = os.path.join(cwd, test_directory)
        if not os.path.exists(path):
            os.mkdir(path)
        self.test_dir_path = path

    def test_setOutputPath(self):
        self.advancedscanner.setOutputPath(self.test_dir_path)
        result = self.advancedscanner.outputPath

        self.assertEqual(self.test_dir_path, result)
    
    def test_setDepth(self):
        depth = 10
        self.advancedscanner.setDepth(depth)
        result = self.advancedscanner.depth
        
        self.assertEqual(depth, result)
    
    def tearDown(self):
        shutil.rmtree(self.test_dir_path, ignore_errors=True)

    
if __name__ == '__main__':
    unittest.main()
