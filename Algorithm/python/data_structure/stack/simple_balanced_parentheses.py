from .Stack import Stack, NoMoreItemException
from unittest import TestCase


class TestBalancedParentheses(TestCase):
    def test_balanced_parentheses(self):
        balanced_string = '(mmsdf(dfdf))'
        self.assertTrue(is_parentheses_balanced(balanced_string))

    def test_unbalanced_parentheses(self):
        no_closed_parentheses_string = '(dfdfjs(lksjdfsld)'
        self.assertFalse(is_parentheses_balanced(no_closed_parentheses_string))
        no_open_parentheses_string = 'dfdfjs(lksjdfsld))'
        self.assertFalse(is_parentheses_balanced(no_open_parentheses_string))


def is_parentheses_balanced(string):
    stack = Stack()
    for c in string:
        if c == '(':
            stack.push(c)
        elif c == ')':
            try:
                stack.pop()
            except NoMoreItemException as e:
                return False
    return True if stack.is_empty() else False
