import os
import sys

sys.path.insert(1, os.path.dirname(os.path.dirname(__file__)))

import unittest
from ratings import *

class TestRatings(unittest.TestCase):
    def test_remove_user_rating(self):
        r1 = Rating(3, 1111)
        r2 = Rating(1, 2222)
        rs = Ratings()
        rs.add_rating(r1)
        rs.add_rating(r2)
        rs.remove_user_rating(2222)
        self.assertEqual(rs.ratings, [r1])
    
    def test_get_sorted_scores(self):
        r1 = Rating(3, 1111)
        r2 = Rating(1, 2222)
        r3 = Rating(5, 3333)
        r4 = Rating(5, 4444)
        rs = Ratings()
        rs.add_rating(r1)
        rs.add_rating(r2)
        rs.add_rating(r3)
        rs.add_rating(r4)
        self.assertEqual(rs.get_sorted_scores(), [1, 0, 1, 0, 2])
    
    def test_to_list(self):
        r1 = Rating(3, 1111)
        r2 = Rating(1, 2222)
        r3 = Rating(5, 3333)
        r4 = Rating(5, 4444)
        rs = Ratings()
        rs.add_rating(r1)
        rs.add_rating(r2)
        rs.add_rating(r3)
        rs.add_rating(r4)
        self.assertEqual(rs.to_list(), [(3, 1111), (1, 2222), (5, 3333), (5, 4444)])