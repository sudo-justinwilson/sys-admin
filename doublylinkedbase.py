class _DoublyLinkedBase:
    """
    A base class providing a doubly linked list representation.
    """

    class _Node:
        """
        A light, non-public class that abstracts a node.
        """
        __slots__ = '_element', '_prev', '_next'        # statically define attrs to streamline memory usage.
        
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """
        Create an empty list.
        """
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer  # trailer is after header
        self._trailer._prev = self._header        # header is before trailer
        self._size = 0

    def __len__(self):
        """
        Return the number of elements in the list.
        """
        return self._size

    def is_empty(self):
        """
        Return True if list is empty.
        """
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """
        Add element e between two existing nodes and return new node.
        """
        newest = self._Node(e, predecessor, successor)  # linked to neighbours
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """
        Delete non-sentinel (not head or tail) node from the list and return its element.
        """
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element                 # store deleted element
        node._prev = node._next = node._element = None      # deprecate node
        return element                  # return deleted element

if __name__ == '__main__':
    dl = _DoublyLinkedBase()
    print('the len: ', len(dl))
