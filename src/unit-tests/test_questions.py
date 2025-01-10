import os
import sys

sys.path.insert(1, os.path.dirname(os.path.dirname(__file__)))

import unittest
from questions import *

class TestQuestions(unittest.TestCase):
    def test_like_question(self):
        q = Question("?", 1234)
        q.like_question(1234)
        q.like_question(2345)
        q.like_question(3456)
        self.assertEqual(q.get_like_count(), 2)
    
    def test_get_questions_sorted(self):
        q1 = Question("?", 1111)
        q2 = Question("??", 2222)
        q3 = Question("???", 3333)
        qs = Questions()
        qs.add_question(q1)
        qs.add_question(q2)
        qs.add_question(q3)
        qs.like_question(1, 2222)
        qs.like_question(1, 3333)
        qs.like_question(2, 3333)
        self.assertEqual(qs.get_questions_sorted(), [q1, q2, q3])
    
    def test_to_list(self):
        q1 = Question("?", 1111)
        q2 = Question("??", 2222)
        q3 = Question("???", 3333)
        qs = Questions()
        qs.add_question(q1)
        qs.add_question(q2)
        qs.add_question(q3)
        qs.like_question(1, 2222)
        qs.like_question(1, 3333)
        qs.like_question(2, 3333)
        self.assertEqual(qs.to_list(), [("?", 1111, [2222, 3333]), ("??", 2222, [3333]), ("???", 3333, [])])
        