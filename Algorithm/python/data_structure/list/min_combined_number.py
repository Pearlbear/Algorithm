from unittest import TestCase
from functools import reduce


class TestMinCombinedNumber(TestCase):
    def test_min_combined_number(self):
        self.assertEqual(min_combined_number([3, 32, 321]), '321323')
        self.assertEqual(min_combined_number([3, 32, 321, 321]), '321321323')
        self.assertEqual(min_combined_number([321]), '321')
        self.assertRaises(EmptyNumbersException, min_combined_number, [])


class CombinedNumber(object):
    def __init__(self, value):
        self.__value = str(value)

    def __lt__(self, other):
        return self.__value + other.value < other.value + self.__value

    def __add__(self, other):
        return CombinedNumber(self.__value + other.value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = str(value)

    def __repr__(self):
        return self.__value


def min_combined_number(numbers):
    if not numbers:
        raise EmptyNumbersException()
    result = []
    for i in range(0, len(numbers)):
        result.append(CombinedNumber(numbers[i]))
    result.sort()
    return (reduce(lambda item, total: item + total, result)).value


class EmptyNumbersException(Exception):
    pass
