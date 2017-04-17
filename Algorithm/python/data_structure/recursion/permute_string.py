from unittest import TestCase


class TestPermuteString(TestCase):
    def test_permute_string(self):
        permutations = permute_string('abc')
        self.assertEqual({'abc', 'acb', 'bac', 'bca', 'cab', 'cba'}, set(permutations))


def permute_string(string):
    def swap(replace_string, index1, index2):
        if index1 == index2:
            return replace_string
        swap_string = list(replace_string)
        swap_string[index1], swap_string[index2] = swap_string[index2], swap_string[index1]
        return ''.join(swap_string)

    if not string:
        return []
    if len(string) == 1:
        return [string]
    if len(string) == 2:
        return [string, swap(string, 0, 1)]
    result = []
    for i in range(0, len(string)):
        replaced = swap(string, 0, i)
        first, rest = replaced[0], replaced[1:]
        result += list(map(lambda item: first + item, permute_string(rest)))
    return result

