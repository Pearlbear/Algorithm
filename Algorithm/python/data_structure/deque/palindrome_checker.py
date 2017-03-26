from .Deque import Deque
from unittest import TestCase


class TestPalindromeChecker(TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('madam'))
        self.assertTrue(is_palindrome('toot'))
        self.assertFalse(is_palindrome('tooth'))
        self.assertFalse(is_palindrome('abcda'))


def is_palindrome(word):
    deque = Deque()
    for c in word:
        deque.add_rear(c)
    while deque.size() > 1:
        rear = deque.remove_rear()
        head = deque.remove_front()
        if rear != head:
            return False
    return True
