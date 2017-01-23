from doublylinkedbase import _DoublyLinkedBase

class LinkedDequeue(_DoublyLinkedBase):
    """
    Double-ended queue implementation based on a doubly linked list.

    Sub-class of __DoublyLinkedBase, and uses its constructor.
    """

    def first(self):
        """
        Return, but do not remove, the first element.
        """
        if self.is_empty():
            raise Empty("Dequeue is empty")
        return self._header._next._element      # the first "real" item after the header

    def last(self):
        """
        Return, but do not remove, the lement at the back of the deque.
        """
        if self.is_empty():
            raise Empty("Dequeue is empty")
        return self._trailer._prev._element     # the last "real" item (real meaning it is not the head or tail), which is before the trailer sentinel

    def insert_first(self, e):
        """
        Add an element to the front of the dequeue.
        """
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """
        Add element e to the back of the queue.
        """
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """
        Remove and return the element from the front of the dequeue.

        else raise Empty.
        """
        if self.is_empty():
            raise Empty("Dequeue is empt")
        return self._delete_node(self._header._next)        # uses an inherited method

    def delete_last(self):
        """
        Remove and return the element from the back of the deque.

        else raise Empty().
        """
        if self.is_empty():
            raise Empty("Dequeue is empty")
        return self._delete_node(self._trailer._prev)       # inherited

if __name__ == '__main__':
    ld = LinkedDequeue()
    print(len(ld))
    ld.insert_first('this was the first element')
    print(len(ld))
    ld.insert_last('this was the last element')
    print(len(ld))
    while len(ld):
        print(ld.delete_first())
    print(len(ld))
