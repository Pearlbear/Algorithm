from unittest import TestCase
from .Stack import Stack


class TestPopOrder(TestCase):
    def test_is_pop_order(self):
        self.assertTrue(is_pop_order([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
        self.assertTrue(is_pop_order([1], [1]))

    def test_not_pop_order(self):
        pop_order_no = [4, 3, 5, 1, 2]
        push_order = [1, 2, 3, 4, 5]
        self.assertFalse(is_pop_order(push_order, pop_order_no))
        self.assertFalse(is_pop_order(push_order, []))
        self.assertFalse(is_pop_order([], pop_order_no))
        self.assertFalse(is_pop_order([1], [2]))


def is_pop_order(push_order, pop_order):
    if not push_order or not pop_order:
        return False
    if len(push_order) != len(pop_order):
        return False
    clone_pop_order = list(pop_order)
    clone_push_order = list(push_order)
    stack = Stack()
    while clone_pop_order:
        if (not stack.is_empty()) and stack.peek() == clone_pop_order[0]:
            stack.pop()
            clone_pop_order.pop(0)
        elif clone_push_order:
            stack.push(clone_push_order.pop(0))
        else:
            return False
    return True
