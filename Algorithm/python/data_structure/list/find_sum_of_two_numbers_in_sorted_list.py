from unittest import TestCase


class TestFindSum(TestCase):
    def test_find_sum_of_two_numbers_in_sorted_list(self):
        self.assertEqual(find_sum_of_two_numbers_in_sorted_list([1, 2, 4, 7, 11, 15], 15), (4, 11))
        self.assertEqual(find_sum_of_two_numbers_in_sorted_list([1, 2], 3), (1, 2))
        self.assertIsNone(find_sum_of_two_numbers_in_sorted_list([1, 2, 4, 7, 11, 15], 25))
        self.assertIsNone(find_sum_of_two_numbers_in_sorted_list([1], 2))
        self.assertIsNone(find_sum_of_two_numbers_in_sorted_list([], 2))


def find_sum_of_two_numbers_in_sorted_list(numbers, sum):
    if not numbers or len(numbers) < 2:
        return None
    head = 0
    rear = len(numbers) - 1
    while rear > head:
        if numbers[head] + numbers[rear] == sum:
            return numbers[head], numbers[rear]
        elif numbers[head] + numbers[rear] > sum:
            rear -= 1
        else:
            head += 1
    return None
