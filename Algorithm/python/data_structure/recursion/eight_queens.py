from unittest import TestCase

"""
八皇后问题，即在棋盘上放置8个皇后，不能在同一行、同一列和同一对角线上。
用一个8位的数组来表示8列，用 0~7 来表示8行，求出这个数组的全排列，则不会在同一行和同一列上，只需检查是否在同一对角线上，即：abs(i - j) != abs(l[i] - l[j])
"""


class TestEightQueens(TestCase):
    def test_eight_queens(self):
        self.assertEqual(len(permute_eight_queens()), 92)


def permute_eight_queens():
    def is_ok(queens):
        for i in range(0, len(queens) - 1):
            for j in range(i + 1, len(queens)):
                if abs(i - j) == abs(queens[i] - queens[j]):
                    return False
        return True

    def exchange(current_candidate, i, j):
        if i == j:
            return current_candidate[:]
        new_list = current_candidate[:]
        new_list[i], new_list[j] = new_list[j], new_list[i]
        return new_list

    def perm(current_candidate, start):
        if start >= len(current_candidate):
            if is_ok(current_candidate):
                result.append(current_candidate)
            return
        for i in range(start, len(current_candidate)):
            exchanged = exchange(current_candidate, start, i)
            perm(exchanged, start + 1)

    result = []
    candidate = [0, 1, 2, 3, 4, 5, 6, 7]
    perm(candidate, 0)
    return result
