from unittest import TestCase


class TestTwoSum(TestCase):
    def test_normal(self):
        self.assertEqual(two_sum([4, 2, 1, 15, 11, 7], 15), (0, 4))

    def test_boundary(self):
        self.assertEqual(two_sum([2, 1], 3), (0, 1))

    def test_exception(self):
        self.assertIsNone(two_sum([4, 2, 1, 15, 11, 7], 25))

    def test_wrong_input(self):
        self.assertIsNone(two_sum([1], 2))
        self.assertIsNone(two_sum([], 2))


def two_sum(nums, target):
    if not nums or len(nums) < 2:
        return None
    dic = {}
    for index, num in enumerate(nums):
        if num in dic:
            return dic[num], index
        else:
            dic[target - num] = index
    return None


def two_sum_in_sorted_list(nums, target):
    if not nums or len(nums) < 2:
        return None
    left_mark = 0
    right_mark = len(nums) - 1
    while right_mark > left_mark:
        if nums[left_mark] + nums[right_mark] == target:
            return nums[left_mark], nums[right_mark]
        elif nums[left_mark] + nums[right_mark] > target:
            right_mark -= 1
        else:
            left_mark += 1
    return None
