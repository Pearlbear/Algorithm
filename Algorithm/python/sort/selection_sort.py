from unittest import TestCase
from random import sample


class TestSort(TestCase):
    def setUp(self):
        self.list = sample(range(0, 1000), 20)

    def test_selection_sort(self):
        sorted_list = selection_sort(self.list)
        for i in range(0, len(sorted_list) - 1):
            self.assertTrue(sorted_list[i] <= sorted_list[i + 1])


def selection_sort(numbers):
    for i in range(0, len(numbers) - 1):
        max_index = 0
        last = len(numbers) - i - 1
        for j in range(1, last):
            if numbers[j] > numbers[max_index]:
                max_index = j
        if numbers[last] < numbers[max_index]:
            numbers[max_index], numbers[last] = numbers[last], numbers[max_index]
    return numbers
