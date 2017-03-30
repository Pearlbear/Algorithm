from unittest import TestCase
from random import sample


class TestSort(TestCase):
    def setUp(self):
        self.list = sample(range(0, 1000), 20)

    def test_selection_sort(self):
        sorted_list = merge_sort(self.list)
        for i in range(0, len(sorted_list) - 1):
            self.assertTrue(sorted_list[i] <= sorted_list[i + 1])


def merge_sort(numbers):
    def merge(start, middle, end):
        sublist1 = numbers[start: middle]
        sublist2 = numbers[middle: end]
        i = 0
        j = 0
        index = start
        while i < len(sublist1) and j < len(sublist2):
            if sublist1[i] < sublist2[j]:
                numbers[index] = sublist1[i]
                i += 1
            else:
                numbers[index] = sublist2[j]
                j += 1
            index += 1
        while i < len(sublist1):
            numbers[index] = sublist1[i]
            index += 1
            i += 1
        while j < len(sublist2):
            numbers[index] = sublist2[j]
            index += 1
            j += 1

    def driver(start, end):
        if end - start > 1:
            middle = (start + end) // 2
            driver(start, middle)
            driver(middle, end)
            merge(start, middle, end)

    driver(0, len(numbers))
    return numbers
