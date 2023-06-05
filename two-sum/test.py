import unittest
from main import twoSum
input_one = [2,7,11,15]
input_two = [3,2,4]
input_three = [3,3]
class TwoStringTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(twoSum(input_one, 9), [0,1])
    def test_two(self):
        self.assertEqual(twoSum(input_two, 6), [1,2])
    def test_three(self):
        self.assertEqual(twoSum(input_three, 6), [0,1])

if __name__ == '__main__':
    unittest.main()
