from unittest import TestCase
from random import sample


class TestReorderArray(TestCase):
    def test_reorder_array(self):
        array = sample(range(0, 1000), 20)
        reorder_array(array, lambda x: True if x & 1 == 1 else False)
        i, j = 0, len(array) - 1
        while i < len(array) and array[i] % 2 == 1:
            i += 1
        while j >= 0 and array[j] % 2 == 0:
            j -= 1
        self.assertEqual(i - j, 1)


def reorder_array(array, ahead):
    head, rear = 0, len(array) - 1
    while head < rear:
        while head < rear and ahead(array[head]):
            head += 1
        while head < rear and not ahead(array[rear]):
            rear -= 1
        if head < rear:
            array[head], array[rear] = array[rear], array[head]
