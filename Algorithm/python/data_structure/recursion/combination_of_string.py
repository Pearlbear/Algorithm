from unittest import TestCase


class TestPermuteString(TestCase):
    def test_permute_string(self):
        ab_combinations = combination_of_string('ab')
        self.assertEqual(len(ab_combinations), 4)
        self.assertEqual({'', 'a', 'b', 'ba'}, set(ab_combinations))
        abc_combinations = combination_of_string('abc')
        self.assertEqual(len(abc_combinations), 8)
        self.assertEqual({'', 'a', 'b', 'c', 'ba', 'cb', 'ca', 'cba'}, set(abc_combinations))


def combination_of_string(string):
    result = []
    n = 1 << len(string)
    for i in range(0, n):
        combination = []
        for j in range(0, len(string)):
            if i & (2 ** j) != 0:
                combination.append(string[-j-1])
        result.append(''.join(combination))
    return result
