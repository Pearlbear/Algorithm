from unittest import TestCase


class TestCount(TestCase):
    def test_count(self):
        self.assertEqual(count_one_in_binary_0(11), 3)
        self.assertEqual(count_one_in_binary_0(-21), 3)
        self.assertEqual(count_one_in_binary_1(11), 3)
        self.assertEqual(count_one_in_binary_1(-21), 30)# 由于整数表示法的不同，python和c的负数二进制表示不一样


def count_one_in_binary_0(number):
    return len(bin(number)[(2 if number > 0 else 3):].replace('0', ''))


def count_one_in_binary_1(number):
    return bin(number & 0xffffffff).count('1')


# def count_one_in_binary_1(number):
#     # 只能用于c语言这种整数有位数限制的
#     count = 0
#     while number != 0:
#         number &= (number - 1)
#         count += 1
#     return count
