from unittest import TestCase


class TestMin(TestCase):
    def test_min(self):
        self.assertEqual(min_number_in_rotated_array((3, 4, 5, 1, 2)), 1)
        self.assertEqual(min_number_in_rotated_array((1, 2, 3, 4, 5)), 1)
        self.assertEqual(min_number_in_rotated_array((1, 0, 1, 1, 1)), 0)
        self.assertEqual(min_number_in_rotated_array((1, 1, 1, 0, 1)), 0)


def min_number_in_rotated_array(rotated_array):
    if not rotated_array:
        return
    head, rear = 0, len(rotated_array) - 1
    while rear - head > 1:
        if rotated_array[rear] > rotated_array[head]:
            return rotated_array[head]
        middle = (rear + head) // 2
        if rotated_array[head] == rotated_array[middle] == rotated_array[rear]:
            return min(rotated_array[head:rear + 1])
        if rotated_array[middle] > rotated_array[head]:
            head = middle
        else:
            rear = middle
    return rotated_array[rear]
