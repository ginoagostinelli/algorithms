from sorting.merge_sort import merge_sort
import unittest

class TestSorting(unittest.TestCase):

    def test_merge_sort(self):
        
        unserted = [5, 9, 40, 5, 2, 1, 9, 22, -5, 0, -62]
        sorted   = [-62, -5, 0, 1, 2, 5, 5, 9, 9, 22, 40]

        self.assertEqual(sorted, merge_sort(unserted))

    if __name__ == '__main__':
        unittest.main()