import unittest

from main import isPalindrome

class ValidPalidromeTest(unittest.TestCase):
    def test_example_one(self):
        self.assertTrue(isPalindrome("racecar"))
    def test_example_two(self):
        self.assertTrue(isPalindrome("A man, a plan, a canal: Panama"))
    def test_example_three(self):
        self.assertTrue(isPalindrome(""))
    def test_example_four(self):
        self.assertFalse(isPalindrome("random string"))



if __name__ == '__main__':
    unittest.main()
