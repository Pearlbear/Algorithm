from unittest import TestCase

"""
求字符串的全组合。
用0、1来代表字符的出现和不出现，因此有 n = 2**len(string) 种组合（包括空字符串），如：abc，100代表a出现，b和c都不出现
"""


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
                combination.append(string[-j - 1])
        result.append(''.join(combination))
    return result
