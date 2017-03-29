from unittest import TestCase
from random import sample


class TestSort(TestCase):
    def setUp(self):
        self.list = sample(range(0, 1000), 20)

    def test_bubble_sort(self):
        sorted_list = shell_sort(self.list)
        for i in range(0, len(sorted_list) - 1):
            self.assertTrue(sorted_list[i] < sorted_list[i + 1])


def shell_sort(numbers):
    increment = len(numbers) // 2
    while increment > 0:
        for i in range(0, increment):
            sub_list = list(range(i, len(numbers), increment))
            for j in range(1, len(sub_list)):
                insert_number = numbers[sub_list[j]]
                insert_index = j
                while insert_number < numbers[sub_list[insert_index - 1]] and insert_index > 0:
                    numbers[sub_list[insert_index]] = numbers[sub_list[insert_index - 1]]
                    insert_index -= 1
                numbers[sub_list[insert_index]] = insert_number
        increment //= 2
    return numbers
