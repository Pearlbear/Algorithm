from unittest import TestCase


class TestPower(TestCase):
    def test_power(self):
        self.assertEqual(power(2, 4), 16)
        self.assertEqual(power(2, 10), 1024)
        self.assertEqual(power(5, 2), 25)
        self.assertEqual(power(5, -2), 1/25)
        self.assertEqual(power(5, 0), 1)

    def test_marginal(self):
        self.assertEqual(power(0, 2), 0)
        self.assertEqual(power(0, 0), 0)
        self.assertEqual(power(0, -2), 0)

    def test_exception(self):
        self.assertRaises(IncorrectInputException, power, 0, 'xxx')
        self.assertRaises(IncorrectInputException, power, 'xxx', 2)
        self.assertRaises(IncorrectInputException, power, 0, 2.1)


def power(base, exponent):
    if not isinstance(exponent, int):
        raise IncorrectInputException('不正确的输入值：exponent = %s', exponent)
    if not isinstance(base, (int, float)):
        raise IncorrectInputException('不正确的输入值：base = %s', base)
    if base == 0:
        return 0
    if exponent == 0:
        return 1

    def driver(b, exp):
        if exp > 1:
            return driver(b * b, exp >> 1) * (1 if exp & 1 == 0 else b)
        else:
            return b
    abs_exponent = abs(exponent)
    result = driver(base, abs_exponent)
    return result if exponent > 0 else 1 / result


class IncorrectInputException(Exception):
    pass
