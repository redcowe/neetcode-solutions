import unittest
from main import isValid

class ValidParantesisTest(unittest.TestCase):
    def test_braces(self):
        self.assertTrue(isValid("[]"))

    def test_brackets(self):
        self.assertTrue(isValid("{}"))

    def test_paranthesis(self):
        self.assertTrue(isValid("()"))

    def test_invalidBraces(self):
        self.assertFalse(isValid("[)"))

    def test_valid_with_different_types_of_paranthesis(self):
        self.assertTrue(isValid("([{}])"))

    def test_one_char_in_string(self):
        self.assertFalse(isValid("}["))

if __name__ == '__main__':
    unittest.main()
