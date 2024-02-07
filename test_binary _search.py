import unittest
from binary_search_ex import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        array = [3, 4, 5, 8, 1, 65, 88, 12]
        find = 88

        result = binary_search(array, find, 0, len(array)-1)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()

