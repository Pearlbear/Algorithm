from unittest import TestCase


class TestClockwise(TestCase):
    def test_clockwise(self):
        matrix_to_clockwise(None)

        row_greater_column = matrix_to_clockwise([
            [1, 14, 13, 12, 11],
            [2, 15, 20, 19, 10],
            [3, 16, 17, 18, 9],
            [4, 5, 6, 7, 8],
        ])
        for i in range(0, len(row_greater_column) - 1):
            self.assertLess(row_greater_column[i], row_greater_column[i + 1])

        row_less_column = matrix_to_clockwise([
            [1, 18, 17, 16, 15],
            [2, 19, 28, 27, 14],
            [3, 20, 29, 26, 13],
            [4, 21, 30, 25, 12],
            [5, 22, 23, 24, 11],
            [6, 7, 8, 9, 10],
        ])
        for i in range(0, len(row_less_column) - 1):
            self.assertLess(row_less_column[i], row_less_column[i + 1])

        row_equal_column_even = matrix_to_clockwise([
            [1, 12, 11, 10],
            [2, 13, 16, 9],
            [3, 14, 15, 8],
            [4, 5, 6, 7],
        ])
        for i in range(0, len(row_equal_column_even) - 1):
            self.assertLess(row_equal_column_even[i], row_equal_column_even[i + 1])

        row_equal_column_singular = matrix_to_clockwise([
            [1, 8, 7],
            [2, 9, 6],
            [3, 4, 5],
        ])
        for i in range(0, len(row_equal_column_singular) - 1):
            self.assertLess(row_equal_column_singular[i], row_equal_column_singular[i + 1])


def matrix_to_clockwise(matrix):
    if not (matrix and len(matrix) and len(matrix[0])):
        return None

    def push_one_circle(current_start):
        end_x = column - start - 1
        end_y = row - start - 1

        for i in range(start, end_x + 1):
            result.append(matrix[i][start])
        if end_y > start:
            for i in range(start + 1, end_y + 1):
                result.append(matrix[end_x][i])
        if start < end_x and start < end_y:
            for i in range(end_x - 1, start - 1, -1):
                result.append(matrix[i][end_y])
        if start < end_x and start < end_y - 1:
            for i in range(end_y - 1, start, -1):
                result.append(matrix[start][i])

    result = []
    start = 0
    column, row = len(matrix), len(matrix[0])
    while (column > start * 2) and (row > start * 2):
        push_one_circle(start)
        start += 1

    return result
