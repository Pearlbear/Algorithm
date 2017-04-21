from unittest import TestCase


class TestFindUglyNumber(TestCase):
    def test_find_ugly_number(self):
        self.assertEqual(find_ugly_number(13), 18)
        self.assertEqual(find_ugly_number(1500), 859963392)


def find_ugly_number(n):
    if n < 0:
        raise IncorrectNegativeInputException()
    ugly_numbers = [1]
    next_index = 1
    ugly_number2_index = 0
    ugly_number3_index = 0
    ugly_number5_index = 0
    while next_index < n:
        next_ugly_number = min(ugly_numbers[ugly_number2_index] * 2, ugly_numbers[ugly_number3_index] * 3,
                               ugly_numbers[ugly_number5_index] * 5)
        ugly_numbers.append(next_ugly_number)
        while ugly_numbers[ugly_number2_index] * 2 <= next_ugly_number:
            ugly_number2_index += 1
        while ugly_numbers[ugly_number3_index] * 3 <= next_ugly_number:
            ugly_number3_index += 1
        while ugly_numbers[ugly_number5_index] * 5 <= next_ugly_number:
            ugly_number5_index += 1
        next_index += 1

    return ugly_numbers[n - 1]


class IncorrectNegativeInputException(Exception):
    pass
