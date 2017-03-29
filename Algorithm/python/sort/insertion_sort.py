from unittest import TestCase
from random import sample


class TestSort(TestCase):
    def setUp(self):
        self.list = sample(range(0, 1000), 20)

    def test_bubble_sort(self):
        sorted_list = insertion_sort(self.list)
        for i in range(0, len(sorted_list) - 1):
            self.assertTrue(sorted_list[i] <= sorted_list[i + 1])


def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        insert_number = numbers[i]
        insert_index = i
        while insert_index > 0 and numbers[insert_index - 1] > insert_number:
            numbers[insert_index] = numbers[insert_index - 1]
            insert_index -= 1
        numbers[insert_index] = insert_number
    return numbers
