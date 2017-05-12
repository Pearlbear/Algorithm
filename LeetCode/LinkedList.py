class Node(object):
    def __init__(self, value, next_node=None):
        self.__value = value
        self.__next = next_node

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
