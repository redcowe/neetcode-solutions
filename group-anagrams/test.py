import unittest

from main import groupAnagrams

class GroupAnagramsTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(groupAnagrams(["eat","tea","tan","ate","nat","bat"]), [["bat"],["nat","tan"],["ate","eat","tea"]])
    def test_two(self):
        self.assertEqual(groupAnagrams(['']), [['']])
    def test_three(self):
        self.assertEqual(groupAnagrams(["a"]),  ["a"])

if __name__ == '__main__':
    unittest.main()
