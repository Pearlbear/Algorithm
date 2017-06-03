from unittest import TestCase


class TestLongestSubstringWithoutRepeatingCharacters(TestCase):
    def test_normal(self):
        self.assertEqual(longest_substring_without_repeating_characters('abcabcbb'), 3)
        self.assertEqual(longest_substring_without_repeating_characters('pwwkew'), 3)
        self.assertEqual(longest_substring_without_repeating_characters('abba'), 2)

    def test_one_char_string(self):
        self.assertEqual(longest_substring_without_repeating_characters('bbbbbb'), 1)

    def test_empty_string(self):
        self.assertEqual(longest_substring_without_repeating_characters(''), 0)
        self.assertEqual(longest_substring_without_repeating_characters(None), 0)


def longest_substring_without_repeating_characters(string):
    if not string:
        return 0
    longest_length = 0
    current_string = ''
    for char in string:
        if char in current_string:
            current_string = current_string[current_string.index(char) + 1:] + char
        else:
            current_string += char
        if longest_length < len(current_string):
            longest_length = len(current_string)
    return longest_length


def longest_substring_without_repeating_characters_optimized(string):
    if not string:
        return 0
    start = longest_length = 0
    used_char = {}
    for i in range(len(string)):
        if string[i] in used_char and start <= used_char[string[i]]:
            start = used_char[string[i]] + 1
        used_char[string[i]] = i
        curr_length = i - start + 1
        if longest_length < curr_length:
            longest_length = curr_length
    return longest_length
