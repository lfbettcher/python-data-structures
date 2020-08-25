# Hash Map implementation with DynamicArray and LinkedList

# Import DynamicArray and LinkedList classes
from dynamic_array import *
from singly_linked_list import *

def hash_function_1(key: str) -> int:
    """ Sample Hash function #1 to be used with A5 HashMap implementation. """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """ Sample Hash function #2 to be used with A5 HashMap implementation. """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """ Init new HashMap based on DA with SLL for collision resolution. """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """ Return content of HashMap in human-readable form. """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """ Clears the contents of the hash map. """
        for i in range(self.buckets.length()):
            self.buckets.set_at_index(i, LinkedList())
        self.size = 0

    def _get_list(self, key: str) -> LinkedList:
        """ Helper method to return the list at the hashed key location. """
        return self.buckets.get_at_index(self.hash_function(key) % self.buckets.length())

    def get(self, key: str) -> object:
        """ Returns value associated with key, or None if key is not in hash map. """
        # get the list at hash location
        list_ = self._get_list(key)

        # get key/value pair
        node = list_.contains(key)
        return None if node is None else node.value

    def put(self, key: str, value: object) -> None:
        """
        Updates the key/value pair in the hash map.
        If the key already exists, the new value replaces the existing value.
        """
        # get the list at hash location
        list_ = self._get_list(key)

        # if key exists, replace value
        node = list_.contains(key)
        if node is not None:
            node.value = value
            return

        # key does not yet exist, add key/value pair
        list_.insert(key, value)
        self.size += 1

    def remove(self, key: str) -> None:
        """
        Removes key and its associated value from hash map,
        or does nothing if key is not in hash map.
        """
        # get the list at hash location
        list_ = self._get_list(key)
        list_.remove(key)
        self.size -= 1

    def contains_key(self, key: str) -> bool:
        """ Returns True if key is in the hash map, otherwise False. """
        # empty hash map does not contain any keys
        if self.size == 0:
            return False

        # get the list at hash location
        list_ = self._get_list(key)
        # return True if list contains key
        return list_.contains(key) is not None

    def empty_buckets(self) -> int:
        """ Returns the number of empty buckets in the hash table. """
        count = 0
        for i in range(self.buckets.length()):
            # check each bucket to see if list is empty
            list_ = self.buckets.get_at_index(i)
            if list_.length() == 0:
                count += 1
        return count

    def table_load(self) -> float:
        """ Returns the current hash table load factor. """
        return self.size / self.buckets.length()

    def resize_table(self, new_capacity: int) -> None:
        """
        Changes the capacity of the internal hash table.
        All existing key/value pairs remain in the new hash map
        and all hash table links are rehashed.
        If the new capacity is less than 1, the method does nothing.
        """
        if new_capacity < 1:
            return

        new_hash_map = HashMap(new_capacity, self.hash_function)

        # iterate through each bucket in hash map
        for i in range(self.buckets.length()):
            list_ = self.buckets.get_at_index(i)
            # iterate through all key/value pairs and rehash into new map
            for node in list_:
                new_hash_map.put(node.key, node.value)

        self.buckets = new_hash_map.buckets
        self.capacity = new_hash_map.capacity

    def get_keys(self) -> DynamicArray:
        """ Returns a DynamicArray that contains all keys stored in the hash map. """
        keys_array = DynamicArray()

        # iterate through each bucket in hash map
        for i in range(self.buckets.length()):
            list_ = self.buckets.get_at_index(i)
            # iterate through all nodes in list and add key to keys array
            for node in list_:
                keys_array.append(node.key)

        return keys_array
