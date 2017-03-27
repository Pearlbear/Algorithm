from unittest import TestCase


class TestReverseString(TestCase):
    def test_reverse(self):
        self.assertEqual(reverse('McGrady'), 'ydarGcM')


def reverse(string):
    head, rest = string[0], string[1:]
    return reverse(rest) + head if rest else head
