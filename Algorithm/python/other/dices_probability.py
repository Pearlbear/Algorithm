from unittest import TestCase


class TestDicesProbability(TestCase):
    def test_dices_probability(self):
        probabilities = dices_probability(3)
        self.assertEqual(probabilities[3], 1)
        self.assertEqual(probabilities[4], 3)
        self.assertEqual(probabilities[5], 6)
        self.assertEqual(probabilities[6], 10)
        self.assertEqual(probabilities[7], 15)
        self.assertEqual(probabilities[8], 21)
        self.assertEqual(probabilities[9], 25)
        self.assertEqual(probabilities[10], 27)
        self.assertEqual(probabilities[11], 27)
        self.assertEqual(probabilities[12], 25)
        self.assertEqual(probabilities[13], 21)
        self.assertEqual(probabilities[14], 15)
        self.assertEqual(probabilities[15], 10)
        self.assertEqual(probabilities[16], 6)
        self.assertEqual(probabilities[17], 3)
        self.assertEqual(probabilities[18], 1)


def dices_probability(n):
    def driver(current):
        if current == 1:
            return {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}
        result = {}
        previous_result = driver(current - 1)
        for i in range(current, current * 6 + 1):
            sum_count = 0
            for j in range(1, 7):
                sum_count += previous_result.get(i - j, 0)
            result[i] = sum_count
        return result

    return driver(n)
