from unittest import TestCase


class TestPermuteString(TestCase):
    def test_permute_string(self):
        ab_permutations = permute_string('ab')
        self.assertEqual(len(ab_permutations), 2)
        self.assertEqual({'ab', 'ba'}, set(ab_permutations))
        abc_permutations = permute_string('abc')
        self.assertEqual(len(abc_permutations), 6)
        self.assertEqual({'abc', 'acb', 'bac', 'bca', 'cab', 'cba'}, set(abc_permutations))
        aac_permutations = permute_string('aac')
        self.assertEqual(len(aac_permutations), 3)
        self.assertEqual({'aac', 'aca', 'caa'}, set(aac_permutations))


def permute_string(string):
    def swap(replace_string, index1, index2):
        if index1 == index2:
            return replace_string
        swap_string = list(replace_string)
        swap_string[index1], swap_string[index2] = swap_string[index2], swap_string[index1]
        return ''.join(swap_string)

    def is_swap(replace_string, index1, index2):
        if index1 == index2:
            return True
        first_to_last_second, last = replace_string[0: index2], replace_string[index2]
        for j in range(0, index2):
            if first_to_last_second[j] == last:
                return False
        return True

    if not string:
        return []
    if len(string) == 1:
        return [string]
    result = []
    for i in range(0, len(string)):
        if is_swap(string, 0, i):
            replaced = swap(string, 0, i)
            first, rest = replaced[0], replaced[1:]
            result += list(map(lambda item: first + item, permute_string(rest)))
    return result
