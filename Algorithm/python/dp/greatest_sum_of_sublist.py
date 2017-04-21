from unittest import TestCase


class TestGreatestSumOfSublist(TestCase):
    def test_greatest_sum_of_sublist(self):
        self.assertEqual(greatest_sum_of_sublist([1, -2, 3, 10, -4, 7, 2, -5]), 18)

    def test_negative_numbers(self):
        self.assertEqual(greatest_sum_of_sublist([-1, -2, -3, -10, -4, -7, -2, -5]), -1)

    def test_positive_numbers(self):
        self.assertEqual(greatest_sum_of_sublist([1, 2, 3, 10, 4, 7, 2, 5]), 34)

    def test_empty_list(self):
        self.assertRaises(IncorrectNumbersException, greatest_sum_of_sublist, [])
        self.assertRaises(IncorrectNumbersException, greatest_sum_of_sublist, None)


# def greatest_sum_of_sublist_recursive(numbers):
#     if not numbers:
#         raise IncorrectNumbersException()
#
#     def sum_of_sublist(end):
#         if end <= 0:
#             return numbers[0], numbers[0]
#         previous_sum_of_sublist, previous_greatest_sum = sum_of_sublist(end - 1)
#         if previous_sum_of_sublist < 0:
#             current_sum_of_sublist = numbers[end]
#             current_greatest_sum = numbers[end] if previous_greatest_sum < numbers[end] else previous_greatest_sum
#             return current_sum_of_sublist, current_greatest_sum
#         else:
#             current_sum_of_sublist = previous_sum_of_sublist + numbers[end]
#             current_greatest_sum = current_sum_of_sublist if previous_greatest_sum < current_sum_of_sublist else previous_greatest_sum
#             return current_sum_of_sublist, current_greatest_sum
#
#     _, greatest_sum = sum_of_sublist(len(numbers) - 1)
#     return greatest_sum


def greatest_sum_of_sublist(numbers):
    if not numbers:
        raise IncorrectNumbersException()

    greatest_sum = numbers[0]
    current_sum = numbers[0]
    for i in range(1, len(numbers)):
        if current_sum < 0:
            current_sum = numbers[i]
        else:
            current_sum += numbers[i]
        if greatest_sum < current_sum:
            greatest_sum = current_sum
    return greatest_sum


class IncorrectNumbersException(Exception):
    pass
