from unittest import TestCase
from random import sample


class TestSort(TestCase):
    def setUp(self):
        self.list = sample(range(0, 1000), 20)

    def test_selection_sort(self):
        sorted_list = quick_sort(self.list)
        for i in range(0, len(sorted_list) - 1):
            self.assertTrue(sorted_list[i] <= sorted_list[i + 1])


def quick_sort(numbers):
    def driver(start, end):
        if end - start < 2:
            return
        if end - start == 2:
            if numbers[start] > numbers[end - 1]:
                numbers[start], numbers[end - 1] = numbers[end - 1], numbers[start]
            return
        pivot = numbers[start]
        left_mark = start + 1
        right_mark = end - 1
        while True:
            if left_mark > right_mark:
                numbers[right_mark], numbers[start] = numbers[start], numbers[right_mark]
                break
            elif numbers[left_mark] > pivot > numbers[right_mark]:
                numbers[left_mark], numbers[right_mark] = numbers[right_mark], numbers[left_mark]
                left_mark += 1
                right_mark -= 1
            elif numbers[right_mark] > pivot:
                right_mark -= 1
            elif numbers[left_mark] < pivot:
                left_mark += 1
        driver(start, right_mark)
        driver(right_mark + 1, end)

    driver(0, len(numbers))
    return numbers
