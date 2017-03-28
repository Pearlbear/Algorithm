from unittest import TestCase


class TestFewestCoins(TestCase):
    def test_fewest_coins(self):
        self.assertEqual(fewest_coins((1, 5, 10, 25), 63), 6)
        self.assertEqual(fewest_coins((1, 5, 10, 21, 25), 63), 3)


# 动态规划比用递归效率更高
def fewest_coins(coin_list, change):
    known = [0] * (change + 1)

    def driver(real_change):
        if known[real_change] > 0:
            return known[real_change]
        if real_change in coin_list:
            known[real_change] = 1
            return 1
        fewest = real_change
        for coin in [c for c in coin_list if c <= real_change]:
            last_coin = driver(real_change - coin) + 1
            if last_coin < fewest:
                fewest = last_coin
                known[real_change] = fewest
        return fewest

    return driver(change)
