import unittest
from classnumberset import MySet


class TestNumberSetCalss(unittest.TestCase):
    def test_insert(self):
        s = MySet()
        self.assertEqual(list(s), [])
        s.insert(1)
        s.insert(11)
        self.assertEqual(sorted(list(s)), [1, 11])

    def test_insert_duplicates(self):
        s = MySet()
        self.assertEqual(list(s), [])
        s.insert(1)
        s.insert(1)
        s.insert(1)
        self.assertEqual(sorted(list(s)), [1])

    def test_delete(self):
        s = MySet()
        self.assertFalse(s.has(1))
        s.delete(1)
        self.assertFalse(s.has(1))
        s.insert(1)
        self.assertTrue(s.has(1))
        s.delete(1)
        self.assertFalse(s.has(1))

    def test_has(self):
        s = MySet()
        self.assertFalse(s.has(1))
        s.insert(1)
        self.assertTrue(s.has(1))

    def test_iterator(self):
        s = MySet()
        s.insert(1)
        s.insert(2)
        s.insert(3)
        self.assertEqual(sorted(list(s)), [1, 2, 3])

    def test_len(self):
        s = MySet()
        self.assertEqual(len(s), 0)
        s.insert(1)
        s.insert(2)
        s.insert(3)
        self.assertEqual(len(s), 3)
        s.delete(3)
        self.assertEqual(len(s), 2)

    def test_str(self):
        s = MySet()
        self.assertEqual(str(s), "{}")
        s.insert(1)
        s.insert(2)
        s.insert(3)

        self.assertEqual(str(s), "{1, 2, 3}")

    def test_union(self):
        set_one = MySet()
        set_two = MySet()

        self.assertEqual(list(set_one.union(set_two)), [])

        for x in range (0,4):
            set_one.insert(x)

        self.assertEqual(list(set_one.union(set_two)), [0, 1, 2, 3])

        for x in range (2,6):
            set_two.insert(x)

        self.assertEqual(list(set_one.union(set_two)), [0, 1, 2, 3, 4, 5])

    def test_intersection(self):
        set_one = MySet()
        set_two = MySet()

        self.assertEqual(list(set_one.intersection(set_two)), [])

        for x in range (0,4):
            set_one.insert(x)

        self.assertEqual(list(set_one.intersection(set_two)), [])

        for x in range (2,6):
            set_two.insert(x)

        self.assertEqual(list(set_one.intersection(set_two)), [2,3])


if __name__ == "__main__":
    unittest.main(exit=False)