from unittest import TestCase
from collections import Counter


class TestIsAnagram(TestCase):
    def test_is_anagram(self):
        self.assertTrue(is_anagram('pythonn', 'typhonn'))
        self.assertTrue(is_anagram('heart', 'earth'))
        self.assertFalse(is_anagram('yaang', 'earth'))


def is_anagram(str1, str2):
    dic1 = {}
    dic2 = {}
    for c in str1:
        dic1[c] = dic1.get(c, 0) + 1
    for c in str2:
        dic2[c] = dic2.get(c, 0) + 1
    return dic1 == dic2


def is_anagram_best_solution(str1, str2):
    return Counter(str1) == Counter(str2)
