from unittest import TestCase


class TestMap(TestCase):
    def setUp(self):
        self.map = Map()

    def test(self):
        self.assertIsNone(self.map.get(34))
        self.map.put(34, 'a')
        self.assertEqual(self.map.get(34), 'a')
        self.map.put(34, 'b')
        self.assertEqual(self.map.get(34), 'b')
        self.assertIsNone(self.map.get(45))
        self.map.put(45, 'c')
        self.assertEqual(self.map.get(45), 'c')


class Map(object):
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, value):
        hash_value = self.__hash_value(key)
        if not self.slots[hash_value]:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        elif self.slots[hash_value] == key:
            self.data[hash_value] = value
        else:
            rehash = self.__rehash(hash_value)
            while True:
                if self.slots[rehash] == key:
                    self.data[rehash] = value
                    break
                if not self.slots[rehash]:
                    self.slots[rehash] = key
                    self.data[rehash] = value
                    break
                rehash = self.__rehash(rehash)

    def get(self, key):
        hash_value = self.__hash_value(key)
        if not self.slots[hash_value]:
            return None
        elif self.slots[hash_value] == key:
            return self.data[hash_value]
        else:
            rehash = self.__rehash(hash_value)
            while True:
                if self.slots[rehash] == key:
                    return self.data[rehash]
                if not self.slots[rehash]:
                    return None
                rehash = self.__rehash(rehash)

    def __hash_value(self, key):
        return key % self.size

    def __rehash(self, old_hash):
        return (old_hash + 1) % self.size
