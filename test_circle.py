"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle

import math
import unittest

class TestCircle(unittest.TestCase):
    # def setup(self):
    #     self.circle = Circle(1)
    def test_add_area_positive(self):
        c1 = Circle(10)
        c2 = Circle(5)
        c_add_area = c1.add_area(c2)
        c_total_area = c1.get_area() + c2.get_area()
        c_total_radius = math.sqrt(c1.get_radius()**2 + c2.get_radius()**2)

        self.assertEquals(c_add_area.get_area(), c_total_area)
        self.assertEquals(c_add_area.get_radius(), c_total_radius)

    def test_add_area_negative(self):
        c1 = Circle(0)
        c2 = Circle(5)
        c_add_area = c1.add_area(c2)
        c_total_area = c1.get_area() + c2.get_area()
        c_total_radius = math.sqrt(c1.get_radius() ** 2 + c2.get_radius() ** 2)

        self.assertEquals(c_add_area.get_area(), c_total_area)
        self.assertEquals(c_add_area.get_radius(), c_total_radius)

    def test_radius_negative(self):
        with self.assertRaises(ValueError):
            c1 = Circle(-5)
            c2 = Circle(-0.7)
