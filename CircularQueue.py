from linkedlists import Empty

class CircularQueue:
    """
    Queue using cirularly linked list for storage.
    """
    #------------ nested _Node class -----------------
    class _Node:
        """
        This is a convenient, lightweight nonpublic class for storing a singly linked node.
        The '__slots__'  statically defines the instance attributes.
        """
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    def __init__(self):
        """
        Create an empty queue.
        """
        self._tail = None
        self._size = 0

    def __len__(self):
        """
        Return the number of elements in queue.
        """
        return self._size

    def is_empty(self):
        """
        Return True if empty.
        """
        return self._size == 0

    def first(self):
        """
        Return, but do not remove, the first element.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size  = 1
        return oldhead._element

    def dequeue(self):
        """
        Remove and return the first element.
        
        Else raise Empty exception.
        """
        if self.is_empty():
            raise Empty('The queue is empty.')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        """
        Add element to the back of the queue.
        """
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        """
        Rotates the queue, moving the element at the front, to the back.
        """
        if self._size > 0:
            self._tail = self._tail._next

if __name__ == '__main__':
    cqueue = CircularQueue()
    cqueue.enqueue('first')
    cqueue.enqueue('third')
    cqueue.enqueue('second')
    print(len(cqueue))
    while len(cqueue):
        print(cqueue.dequeue())
