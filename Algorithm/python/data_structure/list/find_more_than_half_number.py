from unittest import TestCase


class TestFind(TestCase):
    def test_find_more_than_half_number(self):
        self.assertEqual(find_more_than_half_number([1, 2, 3, 2, 2, 2, 5, 4, 2]), 2)
        self.assertEqual(find_more_than_half_number([1, 2, 3, 4, 5, 7, 2, 2, 2]), None)
        self.assertEqual(find_more_than_half_number(None), None)
        self.assertEqual(find_more_than_half_number([]), None)


def find_more_than_half_number(numbers):
    if not numbers:
        return None
    target = numbers[0]
    count = 1
    for current in range(1, len(numbers)):
        if target == numbers[current]:
            count += 1
        else:
            if count > 0:
                count -= 1
            else:
                target = numbers[current]
                count = 1

    def check_target():
        target_count = 0
        for i in range(0, len(numbers)):
            if numbers[i] == target:
                target_count += 1
        if target_count > len(numbers)//2:
            return True
        else:
            return False
    if check_target():
        return target
    else:
        return None
