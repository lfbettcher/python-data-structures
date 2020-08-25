# Data Structures
# Dynamic Array


class DynamicArray:
    """
    Class implementing a Dynamic Array.
    Supported methods are:
    append, pop, swap, get_at_index, set_at_index, length
    """

    def __init__(self, arr=None):
        """ Initialize new dynamic array. """
        self.data = arr.copy() if arr else []

    def __str__(self) -> str:
        """ Return content of dynamic array in human-readable form. """
        return str(self.data)

    def append(self, value: object) -> None:
        """ Add new element at the end of the array. """
        self.data.append(value)

    def pop(self) -> object:
        """ Removes element from end of the array and return it. """
        return self.data.pop()

    def swap(self, i: int, j: int) -> None:
        """ Swaps values of two elements given their indexes. """
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def get_at_index(self, index: int) -> object:
        """ Return value of element at a given index. """
        return self.data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """ Set value of element at a given index. """
        self.data[index] = value

    def length(self) -> int:
        """ Return the length of the dynamic array. """
        return len(self.data)
