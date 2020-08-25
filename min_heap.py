# Min Heap implementation with DynamicArray

# Import DynamicArray class
from dynamic_array import *


class MinHeapException(Exception):
    """ Custom exception to be used by MinHeap class. """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """ Initializes a new MinHeap. """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """ Return MinHeap content in human-readable form. """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """ Return True if no elements in the heap, otherwise False. """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """ Adds new object to MinHeap. """
        # add new element at end of array
        self.heap.append(node)

        index = self.heap.length() - 1
        # do not continue if beginning of array
        while index > 0:
            # compute new element's parent index
            parent_index = (index - 1) // 2

            # if value of parent is greater than new element, swap the elements
            if self.heap.get_at_index(parent_index) > self.heap.get_at_index(index):
                self.heap.swap(parent_index, index)

            # repeat with next parent until beginning of array
            index = parent_index

    def get_min(self) -> object:
        """
        Returns object with minimum key without removing from heap.
        Raises MinHeapException if heap is empty.
        """
        if self.is_empty():
            raise MinHeapException
        return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        Returns object with minimum key and removes it from the heap.
        Raise MinHeapException if heap is empty.
        """
        if self.is_empty():
            raise MinHeapException

        # remember value of first element, to be returned
        min_object = self.heap.get_at_index(0)

        # replace value of first element with value of last element
        last_value = self.heap.get_at_index(self.heap.length() - 1)
        self.heap.set_at_index(0, last_value)
        # remove last element
        self.heap.pop()

        # percolate down the new replacement element
        self._percolate_down(0)
        return min_object

    def _percolate_down(self, index: int) -> None:
        """ Helper method to percolate an element at given index down. """
        N = self.heap.length()
        while 0 <= index < N:
            cur_value = self.heap.get_at_index(index)
            swap_child = -1
            left_index = 2 * index + 1
            right_index = 2 * index + 2
            left_value = None
            right_value = None

            # get values of children if they exist
            if left_index < N:
                left_value = self.heap.get_at_index(left_index)
            if right_index < N:
                right_value = self.heap.get_at_index(right_index)

            # if right child exists, so does left, swap if less than current value
            if right_value is not None and right_value < cur_value:
                # swap with the lesser of two children
                swap_child = left_index if left_value < right_value else right_index
            # if left child is less than current, swap with left child
            elif left_value is not None and left_value < cur_value:
                swap_child = left_index

            if swap_child >= 0:
                self.heap.swap(index, swap_child)

            # continue down tree if swap occurred
            index = swap_child

    def build_heap(self, da: DynamicArray) -> None:
        """ Builds a MinHeap from a dynamic array and replaces current MinHeap. """
        # make a copy of input array so it is not modified
        da_copy = DynamicArray()
        for i in range(da.length()):
            da_copy.append(da.get_at_index(i))
        self.heap = da_copy

        # find first non-leaf node (floor of n/2 - 1)
        index = (self.heap.length() // 2 - 1)
        # move up the tree while percolating elements down
        while index >= 0:
            self._percolate_down(index)
            index -= 1
