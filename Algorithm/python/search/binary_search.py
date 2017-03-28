from unittest import TestCase


class TestBinarySearch(TestCase):
    def test_binary_search(self):
        self.assertTrue(binary_search((1, 4, 7, 13, 23, 34, 41, 57, 69, 78, 79, 90, 92), 79))
        self.assertFalse(binary_search((1, 4, 7, 13, 23, 34, 41, 57, 69, 78, 79, 90, 92), 91))


def binary_search(items, item):
    head, rear = 0, len(items) - 1
    while head <= rear:
        middle = (head + rear) // 2
        if item == items[middle]:
            return True
        elif item < items[middle]:
            rear = middle - 1
        else:
            head = middle + 1
    return False
