from unittest import TestCase


class TestFindNumbersAppearOnce(TestCase):
    def test_find_numbers_appear_once(self):
        self.assertTrue(find_numbers_appear_once([2, 4, 3, 6, 3, 2, 5, 5]) == {4, 6})
        self.assertTrue(find_numbers_appear_once([4, 6]) == {4, 6})


def find_numbers_appear_once(numbers):
    xor_result = numbers[0]
    for i in range(1, len(numbers)):
        xor_result ^= numbers[i]
    first_index_of_1 = bin(xor_result)[::-1].index('1')
    and_number = 1 << first_index_of_1

    appear_once_num1, appear_once_num2 = 0, 0

    for i in range(0, len(numbers)):
        if numbers[i] & and_number:
            appear_once_num1 ^= numbers[i]
        else:
            appear_once_num2 ^= numbers[i]

    return {appear_once_num1, appear_once_num2}
