# Data Structures
# Singly Linked List


class SLNode:
    def __init__(self, key: str, value: object) -> None:
        """ Singly Linked List Node class. """
        self.next = None
        self.key = key
        self.value = value

    def __str__(self):
        """ Return content of the node in human-readable form. """
        return '(' + str(self.key) + ': ' + str(self.value) + ')'


class LinkedList:
    """
    Class implementing a Singly Linked List.
    Supported methods are: insert, remove, contains, length, iterator.
    """

    def __init__(self) -> None:
        """ Init new SLL. """
        self.head = None
        self.size = 0

    def __str__(self) -> str:
        """ Return content of SLL in human-readable form. """
        content = ''
        if self.head is not None:
            content = str(self.head)
            cur = self.head.next
            while cur is not None:
                content += ' -> ' + str(cur)
                cur = cur.next
        return 'SLL [' + content + ']'

    def insert(self, key: str, value: object) -> None:
        """ Insert new node at the beginning of the list. """
        new_node = SLNode(key, value)
        new_node.next = self.head
        self.head = new_node
        self.size = self.size + 1

    def remove(self, key: str) -> bool:
        """ Remove first node with matching key. """
        prev, cur = None, self.head
        while cur is not None:
            if cur.key == key:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                self.size -= 1
                return True
            prev, cur = cur, cur.next
        return False

    def contains(self, key: str) -> SLNode:
        """
        If node with matching key in the list -> return pointer
        to that node (SLNode), otherwise return None.
        """
        cur = self.head
        while cur is not None:
            if cur.key == key:
                return cur
            cur = cur.next
        return cur

    def length(self) -> int:
        """ Return the length of the list. """
        return self.size

    def __iter__(self) -> SLNode:
        """
        Provides iterator capability for the SLL class
        so it can be used in for ... in ... type of loops.
        EXAMPLE:
            for node in my_list:
                print(node.key, node.value)
        """
        cur = self.head
        while cur is not None:
            yield cur
            cur = cur.next
