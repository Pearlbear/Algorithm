from unittest import TestCase
from LinkedList import Node


class TestAddTwoNumbers(TestCase):
    def test_normal(self):
        result = add_two_numbers(Node(2, Node(4, Node(3))), Node(5, Node(6, Node(4))))
        self.assertEqual(result.value, 7)
        self.assertEqual(result.next.value, 0)
        self.assertEqual(result.next.next.value, 8)

    def test_zero(self):
        result = add_two_numbers(Node(2, Node(4, Node(3))), Node(0))
        self.assertEqual(result.value, 2)
        self.assertEqual(result.next.value, 4)
        self.assertEqual(result.next.next.value, 3)

    def test_none(self):
        result = add_two_numbers(Node(2, Node(4, Node(3))), None)
        self.assertEqual(result.value, 2)
        self.assertEqual(result.next.value, 4)
        self.assertEqual(result.next.next.value, 3)


def add_two_numbers(l1, l2):
    def add_digit(node1, node2, carry):
        if not (node1 or node2 or carry):
            return None
        sum_result = carry
        next_node1, next_node2 = None, None
        if node1:
            sum_result += node1.value
            next_node1 = node1.next
        if node2:
            sum_result += node2.value
            next_node2 = node2.next
        next_carry, current_value = divmod(sum_result, 10)
        return Node(current_value, add_digit(next_node1, next_node2, next_carry))

    return add_digit(l1, l2, 0)
