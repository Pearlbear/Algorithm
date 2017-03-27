from unittest import TestCase


class TestPalindromeChecker(TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('madam'))
        self.assertTrue(is_palindrome('aibohphobia'))
        self.assertFalse(is_palindrome('tooth'))
        self.assertFalse(is_palindrome('abcda'))


def is_palindrome(word):
    if len(word) <= 1:
        return True
    return word[0] == word[-1] and is_palindrome(word[1: -1])
