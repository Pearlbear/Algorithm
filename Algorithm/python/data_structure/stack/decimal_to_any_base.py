from .Stack import Stack
from unittest import TestCase


class TestDecimalToAnyBase(TestCase):
    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_any_base(78), '1001110')
        self.assertEqual(decimal_to_any_base(79), '1001111')

    def test_decimal_to_octal(self):
        self.assertEqual(decimal_to_any_base(78, 8), '116')

    def test_decimal_to_hexadecimal(self):
        self.assertEqual(decimal_to_any_base(233, 16), 'E9')


def decimal_to_any_base(number, base=2):
    digits = "0123456789ABCDEF"
    stack = Stack()
    quotient = number
    while quotient > 0:
        stack.push(quotient % base)
        quotient //= base
    result = ''
    while not stack.is_empty():
        result += digits[stack.pop()]
    return result
