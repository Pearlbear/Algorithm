from unittest import TestCase


class TestCountKInSortedList(TestCase):
    def test_count(self):
        self.assertEqual(count_k_in_sorted_list([1, 2, 3, 3, 3, 3, 4, 5], 3), 4)
        self.assertEqual(count_k_in_sorted_list([1, 2, 3, 3, 3, 3, 4, 5], 2), 1)
        self.assertEqual(count_k_in_sorted_list([1, 1, 2, 2, 3, 3, 3], 3), 3)
        self.assertEqual(count_k_in_sorted_list([1, 1, 2, 2, 3, 3, 3], 1), 2)
        self.assertEqual(count_k_in_sorted_list([1, 1, 2, 2, 3, 3, 3], 2), 2)
        self.assertEqual(count_k_in_sorted_list([1, 1, 2, 2, 3, 3, 3], 4), 0)
        self.assertEqual(count_k_in_sorted_list([2, 2, 3, 3, 3, 4, 4], 1), 0)
        self.assertEqual(count_k_in_sorted_list([1], 1), 1)
        self.assertEqual(count_k_in_sorted_list([1], 2), 0)
        self.assertEqual(count_k_in_sorted_list([], 1), 0)


def count_k_in_sorted_list(numbers, k):
    if not numbers:
        return 0

    def get_first(start, end):
        if end - start < 0:
            return -1
        middle = (end + start) // 2
        if numbers[middle] == k:
            if middle == 0:
                return middle
            previous = numbers[middle - 1]
            if previous != k:
                return middle
            else:
                return get_first(start, middle - 1)
        elif numbers[middle] > k:
            return get_first(start, middle - 1)
        else:
            return get_first(middle + 1, end)

    def get_last(start, end):
        if end - start < 0:
            return -1
        middle = (end + start) // 2
        if numbers[middle] == k:
            if middle == len(numbers) - 1:
                return middle
            next = numbers[middle + 1]
            if next != k:
                return middle
            else:
                return get_last(middle + 1, end)
        elif numbers[middle] > k:
            return get_last(start, middle - 1)
        else:
            return get_last(middle+1, end)

    first_k_index = get_first(0, len(numbers)-1)
    last_k_index = get_last(0, len(numbers)-1)

    if first_k_index >= 0 and last_k_index >= 0:
        return last_k_index - first_k_index + 1
    else:
        return 0
