from unittest import TestCase


class TestFind(TestCase):
    def test_find(self):
        matrix = [[1, 2, 4, 6], [2, 4, 7, 8], [8, 9, 10, 11], [9, 12, 13, 15]]
        self.assertTrue(find_in_partially_sorted_matrix(matrix, 7))
        self.assertFalse(find_in_partially_sorted_matrix(matrix, 14))


def find_in_partially_sorted_matrix(matrix, target):
    current_row = 0
    current_column = len(matrix) - 1
    while current_row < len(matrix[0]) and current_column >= 0:
        current_num = matrix[current_column][current_row]
        if target == current_num:
            return True
        elif target < current_num:
            current_column -= 1
        else:
            current_row += 1
    return False