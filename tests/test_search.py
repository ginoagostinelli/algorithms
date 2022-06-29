from search.binary_search import binary_search 
import unittest

class TestSearch(unittest.TestCase):

    def test_binary_search(self):
        array = [1, 2, 2, 3, 4, 5, 5, 6, 7, 20]

        self.assertEqual(0, binary_search(array, 1))
        self.assertEqual(9, binary_search(array, 20))
        self.assertEqual(4, binary_search(array, 4))
        self.assertEqual(-1, binary_search(array, 8))
        self.assertEqual(-1, binary_search(array, 25))

    if __name__ == '__main__':
        unittest.main()
