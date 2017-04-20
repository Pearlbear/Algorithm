import heapq
from unittest import TestCase


class TestFindKLeastNumbers(TestCase):
    def test_find(self):
        result = find_k_least_numbers([4, 5, 1, 6, 2, 7, 3, 8], 4)
        result.sort()
        self.assertTrue(result == [1, 2, 3, 4])

    def test_find_in_same_numbers(self):
        result = find_k_least_numbers([4, 5, 1, 6, 2, 7, 3, 3, 8], 4)
        result.sort()
        self.assertTrue(result == [1, 2, 3, 3])

    def test_k_equal_one(self):
        result = find_k_least_numbers([4, 5, 1, 6, 2, 7, 3, 8], 1)
        self.assertTrue(result == [1])

    def test_k_equal_length(self):
        result = find_k_least_numbers([4, 5, 1, 6, 2, 7, 3, 8], 8)
        result.sort()
        self.assertTrue(result == [1, 2, 3, 4, 5, 6, 7, 8])

    def test_k_greater_than_length(self):
        self.assertRaises(IncorrectKException, find_k_least_numbers, [4, 5, 1, 6], 5)

    def test_k_less_than_zero(self):
        self.assertRaises(IncorrectKException, find_k_least_numbers, [4, 5, 1, 6], 0)
        self.assertRaises(IncorrectKException, find_k_least_numbers, [4, 5, 1, 6], -1)

    def test_null_numbers(self):
        self.assertRaises(EmptyNumbersException, find_k_least_numbers, [], 3)
        self.assertRaises(EmptyNumbersException, find_k_least_numbers, None, 2)


def find_k_least_numbers(numbers, k):
    if k < 1:
        raise IncorrectKException()
    if not numbers:
        raise EmptyNumbersException()
    if k > len(numbers):
        raise IncorrectKException()
    if k == len(numbers):
        return numbers[:]
    if k == 1:
        def find_min(number_list):
            min_number = number_list[0]
            for i in range(1, len(number_list)):
                if number_list[i] < min_number:
                    min_number = number_list[i]
            return [min_number]
        return find_min(numbers)
    heap = MaxHeap()
    for i in range(0, k):
        heap.push(numbers[i])
    for i in range(k, len(numbers)):
        if numbers[i] < heap.find_max():
            heap.push(numbers[i])
            heap.del_max()
    return [heap.del_max() for i in range(0, k)]


class MaxHeap(object):
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, -item)

    def find_max(self):
        return -self.heap[0]

    def del_max(self):
        return -heapq.heappop(self.heap)


class IncorrectKException(Exception):
    pass


class EmptyNumbersException(Exception):
    pass
