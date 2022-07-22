from searching.binary_search import binary_search, binary_search_by_recursion
import unittest

class TestSearch(unittest.TestCase):

    def test_binary_search(self):
        array = [1, 2, 2, 3, 4, 5, 5, 6, 7, 20]

        self.assertEqual(0, binary_search(array, 1))
        self.assertEqual(9, binary_search(array, 20))
        self.assertEqual(4, binary_search(array, 4))
        self.assertEqual(-1, binary_search(array, 8))
        self.assertEqual(-1, binary_search(array, 25))

        # Test binary_search_by_recursion 
        l = 0
        r = len(array) - 1

        self.assertEqual(0, binary_search_by_recursion(array, 1, l, r))
        self.assertEqual(9, binary_search_by_recursion(array, 20, l, r))
        self.assertEqual(4, binary_search_by_recursion(array, 4, l, r))
        self.assertEqual(-1, binary_search_by_recursion(array, 8, l, r))
        self.assertEqual(-1, binary_search_by_recursion(array, 25, l, r))

    if __name__ == '__main__':
        unittest.main()
