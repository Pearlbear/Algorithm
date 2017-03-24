from .Stack import Stack
from unittest import TestCase


class TestEvaluatePostfix(TestCase):
    def test_evaluate_correct(self):
        self.assertEqual(evaluate_postfix('7 8 + 3 2 + /'), 3)


def evaluate_postfix(postfix):
    stack = Stack()
    postfix_list = postfix.split()
    for ope in postfix_list:
        if ope in '+-*/':
            number2 = int(stack.pop())
            number1 = int(stack.pop())
            if ope == '+':
                stack.push(number1 + number2)
            elif ope == '-':
                stack.push(number1 - number2)
            elif ope == '*':
                stack.push(number1 * number2)
            elif ope == '/':
                stack.push(number1 / number2)
        else:
            stack.push(ope)
    return stack.pop()
