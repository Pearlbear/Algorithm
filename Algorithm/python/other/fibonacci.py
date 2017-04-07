from unittest import TestCase


class TestFibonacci(TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)

def fibonacci(n):
    def driver(a, b, count):
        if count == 0:
            return b
        else:
            return driver(a + b, a, count - 1)
    return driver(1, 0, n)
