from .Stack import Stack, NoMoreItemException
from unittest import TestCase


class TestBalancedSymbols(TestCase):
    def setUp(self):
        self.symbols = {'open': '([{', 'close': ')]}'}

    def test_balanced_symbols(self):
        balanced_string = '(mms[df(df{df})])'
        self.assertTrue(is_symbols_balanced(balanced_string, self.symbols))

    def test_unbalanced_symbols(self):
        no_closed_parentheses_string = '([d{fdfjs(lksjdfsld)}]'
        self.assertFalse(is_symbols_balanced(no_closed_parentheses_string, self.symbols))
        no_open_parentheses_string = '[dfd{fjs(lksjdf)}sld])'
        self.assertFalse(is_symbols_balanced(no_open_parentheses_string, self.symbols))
        parentheses_incorrect_order_string = '[dfd{fjs(lksjdf)]}'
        self.assertFalse(is_symbols_balanced(parentheses_incorrect_order_string, self.symbols))


def is_symbols_balanced(string, symbols):
    stack = Stack()
    for c in string:
        if c in symbols['open']:
            stack.push(c)
        elif c in symbols['close']:
            try:
                symbol = stack.pop()
                if symbols['open'].index(symbol) != symbols['close'].index(c):
                    return False
            except NoMoreItemException as e:
                return False
    return True if stack.is_empty() else False
