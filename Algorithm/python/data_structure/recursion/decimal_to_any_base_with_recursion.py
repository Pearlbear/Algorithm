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
    if number == 0:
        return ''
    return decimal_to_any_base(number // base, base) + digits[number % base]