import unittest
from has_next_iterator import HasNextIterator


class TestHasNextIterator(unittest.TestCase):
    def test_has_next_iterator(self):
        nums = HasNextIterator(iter([1, 2, 3, 4, 5]))
        self.assertEqual(list(nums), [1, 2, 3, 4, 5])

    def test_has_next_method(self):
        nums_1 = HasNextIterator(iter([]))
        self.assertFalse(nums_1.has_next())

        nums = HasNextIterator(iter([1, 2, 3]))
        self.assertTrue(nums.has_next())
        self.assertEqual(next(nums), 1)

        self.assertTrue(nums.has_next())
        self.assertEqual(next(nums), 2)

        self.assertTrue(nums.has_next())
        self.assertEqual(next(nums), 3)

        self.assertFalse(nums.has_next())
        self.assertFalse(nums.has_next())

    def test_next_method_exception(self):
        nums = HasNextIterator(iter([1, 2, 3]))

        next(nums)
        next(nums)
        next(nums)

        with self.assertRaises(StopIteration):
            next(nums)


if __name__ == "__main__":
    unittest.main()