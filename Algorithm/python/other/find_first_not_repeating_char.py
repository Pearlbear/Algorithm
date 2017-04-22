from unittest import TestCase
from collections import Counter


class TestFindFirstNotRepeatingChar(TestCase):
    def test_find_first_not_repeating_char(self):
        self.assertEqual(find_first_not_repeating_char('abaccdeff'), 'b')
        self.assertRaises(NoSingleCharException, find_first_not_repeating_char, 'aaccddff')
        self.assertRaises(EmptyStringException, find_first_not_repeating_char, '')


def find_first_not_repeating_char(string):
    if not string:
        raise EmptyStringException()
    count = Counter(string)
    for i in range(0, len(string)):
        if count[string[i]] == 1:
            return string[i]
    raise NoSingleCharException()


class EmptyStringException(Exception):
    pass


class NoSingleCharException(Exception):
    pass
