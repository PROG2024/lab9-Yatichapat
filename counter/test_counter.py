"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import unittest
from counter import Counter


class TestCounter(unittest.TestCase):
    def test_singleton(self):
        c1 = Counter()
        self.assertEquals(1, c1.count)
        c1.increment()
        c2 = Counter()
        self.assertEquals(2, c2.count)
