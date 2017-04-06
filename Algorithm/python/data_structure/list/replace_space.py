from unittest import TestCase


class TestReplaceSpace(TestCase):
    def test_replace_space(self):
        self.assertEqual(replace_space('Hello world!'), 'Hello%20world!')


def replace_space(string):
    space_count = 0
    for c in string:
        if c == ' ':
            space_count += 1
    new_string_length = len(string) + space_count * 2
    new_string_list = [''] * new_string_length
    index = len(string) - 1
    new_string_index = len(new_string_list) - 1
    while index >= 0:
        if string[index] == ' ':
            new_string_list[new_string_index] = '0'
            new_string_list[new_string_index - 1] = '2'
            new_string_list[new_string_index - 2] = '%'
            new_string_index -= 3
            index -= 1
        else:
            new_string_list[new_string_index] = string[index]
            new_string_index -= 1
            index -= 1
    return ''.join(new_string_list)
