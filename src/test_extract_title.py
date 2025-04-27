import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_eq(self):
        md = """
# Easy Peasy
"""
        header = extract_title(md)
        self.assertEqual('Easy Peasy', header)
#leading and trailing spaces
    def test_eq2(self):
        md = """
#  Easy Peasy   
"""
        header = extract_title(md)
        self.assertEqual('Easy Peasy', header)
# checking for Exception
    def test_failure(self):
        md = """
##  Easy Peasy   
""" 
        with self.assertRaises(Exception):
            extract_title(md)
   