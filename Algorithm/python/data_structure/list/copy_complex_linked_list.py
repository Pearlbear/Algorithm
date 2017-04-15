from unittest import TestCase


class TestCopy(TestCase):
    def test_copy_complex_linked_list(self):
        a = ListNode('A')
        b = ListNode('B')
        c = ListNode('C')
        d = ListNode('D')
        e = ListNode('E')
        a.next = b
        a.sibling = c
        b.next = c
        b.sibling = e
        c.next = d
        d.next = e
        d.sibling = b
        complex_linked_list = a
        cloned_complex_linked_list = copy_complex_linked_list(complex_linked_list)
        self.assertEqual(cloned_complex_linked_list.value, 'A')
        self.assertEqual(cloned_complex_linked_list.next.value, 'B')
        self.assertEqual(cloned_complex_linked_list.next.next.value, 'C')
        self.assertEqual(cloned_complex_linked_list.next.next.next.value, 'D')
        self.assertEqual(cloned_complex_linked_list.next.next.next.next.value, 'E')
        self.assertEqual(cloned_complex_linked_list.sibling.value, 'C')
        self.assertEqual(cloned_complex_linked_list.next.sibling.value, 'E')
        self.assertEqual(cloned_complex_linked_list.next.next.next.sibling.value, 'B')


def copy_complex_linked_list(linked_list):
    if not linked_list:
        return None
    
    def copy_every_node(head_node):
        current_node = head_node
        while current_node:
            cloned_node = ListNode(current_node.value)
            cloned_node.next = current_node.next
            current_node.next = cloned_node
            current_node = cloned_node.next
        return head_node

    def set_sibling(head_node):
        current_node = head_node
        while current_node:
            if current_node.sibling:
                current_node.next.sibling = current_node.sibling.next
            current_node = current_node.next.next

    copied_list = copy_every_node(linked_list)
    set_sibling(copied_list)
    original_list = copied_list
    new_list = copied_list.next
    current_original_list_node = original_list
    current_new_list_node = new_list
    while current_original_list_node:
        current_original_list_node.next = current_original_list_node.next.next
        current_original_list_node = current_original_list_node.next
        if current_new_list_node.next:
            current_new_list_node.next = current_new_list_node.next.next
            current_new_list_node = current_new_list_node.next
    return new_list


class ListNode(object):
    def __init__(self, value, next_node=None, sibling=None):
        self.__value = value
        self.__next = next_node
        self.__sibling = sibling

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_node):
        self.__next = next_node

    @property
    def sibling(self):
        return self.__sibling

    @sibling.setter
    def sibling(self, sibling):
        self.__sibling = sibling
