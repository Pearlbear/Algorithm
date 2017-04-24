from unittest import TestCase


class TestSequence(TestCase):
    def test_find_continuous_sequence_with_sum(self):
        sequence = find_continuous_sequence_with_sum(9)
        self.assertTrue(sequence[0], [2, 3, 4])
        self.assertTrue(sequence[1], [4, 5])
        self.assertTrue(find_continuous_sequence_with_sum(3), [1, 2])
        self.assertEqual(len(find_continuous_sequence_with_sum(4)), 0)


def find_continuous_sequence_with_sum(sum):
    if sum < 3:
        return []

    def sum_sequence(first, end):
        return (first + end) * (end - first + 1) / 2

    result = []
    head, rear = 1, 2
    while head < rear:
        sequence_sum = sum_sequence(head, rear)
        if sequence_sum == sum:
            result.append([x for x in range(head, rear + 1)])
            head += 1
            rear += 1
        elif sequence_sum > sum:
            head += 1
        else:
            rear += 1
    return result
