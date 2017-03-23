from .Stack import Stack
from unittest import TestCase


class TestInfixToPostfix(TestCase):
    def test_infix_to_postfix(self):
        self.assertEqual(infix_to_postfix('a + b'), 'a b +')
        self.assertEqual(infix_to_postfix('A * B + C * D'), 'A B * C D * +')
        self.assertEqual(infix_to_postfix('A * ( B + C )'), 'A B C + *')
        self.assertEqual(infix_to_postfix('( A + B ) * C - ( D - E ) * ( F + G )'), 'A B + C * D E - F G + * -')


def infix_to_postfix(infix):
    """
    中缀转后缀规则：
    1. 如果是操作数，直接添加到结果列表尾部
    2. 如果是左括弧，将其放入栈中
    3. 如果是右括弧，弹出栈中的操作符，添加到结果列表尾部，直到左括弧为止
    4. 如果是操作符，将其放入栈中，放入之前先将栈中已有的操作符弹出并添加到结果列表尾部，直到比这个操作符更低级的操作符为止
    5. 最后将栈中所有操作符弹出，添加到结果列表尾部
    :param infix:
    :return: postfix:
    """
    level = {
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }
    ops = Stack()
    result = []
    infix_list = infix.split()
    for c in infix_list:
        if c == '(':
            ops.push(c)
        elif c == ')':
            while True:
                last = ops.pop()
                if last == '(':
                    break
                else:
                    result.append(last)
        elif c in '+-*/':
            while not ops.is_empty():
                last = ops.peek()
                if level[c] > level[last]:
                    break
                else:
                    result.append(ops.pop())
            ops.push(c)
        else:
            result.append(c)
    while not ops.is_empty():
        result.append(ops.pop())
    return ' '.join(result)
