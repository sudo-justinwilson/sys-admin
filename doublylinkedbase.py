from linkedlists import Empty

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

###         ---     SUB-CLASS   ###         ---     
###         ---     SUB-CLASS   ###         ---     

class LinkedDeque(_DoublyLinkedBase):
    """
    Double-ended queue implementation based on a doubly linked list.
    """

    def first(self):
        """
        Return, but do not remove, the element at the front of the dequeue.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element

    def last(self):
        """
        Return, but do not remove, the element at the back of the dequeue.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element

    def insert_first(self, e):
        """
        Add an element to the front of the deque.
        """
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """
        Add an element to the back of the deque.
        """
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """
        Remove and return the element from the front of the deque.

        Else raise exception.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._header._next)    # uses inherited method

    def delete_last(self):
        """
        Remove and return the element from the back of the deque.

        else raise exception.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev)



if __name__ == '__main__':
    ld = LinkedDeque()
    print('the len: ', len(ld))
    ld.insert_first('insert first')
    print('the len: ', len(ld))
    print('first = ', ld.first())
    ld.insert_last('insert last')
    print('the len: ', len(ld))
    print('last = ', ld.last())
    ld.delete_first()
    print('the len after delete_first: ', len(ld))
    print('first = ', ld.first())
    ld.delete_last()
    print('the len after delete_last: ', len(ld))
    print('last = ', ld.last())
    print('the len: ', len(ld))
