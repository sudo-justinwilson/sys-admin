class Empty(Exception):
    """
    This error is raised when an attempt is made to access an element from an empty list.
    """

class LinkedStack:
    """
    LIFO Stack implementation using a singly linked list for storage.

    This is from page 263 of the book.
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

    #------------ stack methods----------------
    def __init__(self):
        """
        initialize an empty stack.
        """
        self._head = None           # this is the head node
        self._size = 0              # this keeps a count of the number of stack elements
    
    def __len__(self):
        """
        this returns the number of elements in the stack.
        """
        return self._size

    def is_empty(self):
        """
        True if the stack is empty.
        """
        return self._size == 0

    def push(self, e):
        """
        Add element to the top of the stack.
        """
        self._head = self._Node(e, self._head)          # this creates and links a new node
        self._size += 1

    def top(self):
        """
        Return, but do not remove, the element at the top of the stack.
        
        Will Taise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element          # top of stack is at head of list

    def pop(self):
        """
        Remove and return the element from the top of the stack (ie: LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next           # bypass the former to node
        self._size -= 1
        return answer

##  ++++++++    NEW CLASS
##  ++++++++    NEW CLASS

class LinkedQueue:
    """
    FIFO queueimplementation using a singly linked list for storage.
    """

    # ------------- nested class
    class _Node:
        """
        Lightweight, nonpublic class for storing a singly linked node.
        """
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """
        Create an empty queue.
        """
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """
        Return the number of elements in the queue.
        """
        return self._size

    def is_empty(self):
        """
        Return True if the queue is empty.
        """
        return self._size == 0

    def first(self):
        """
        Return, but do not remove the element at the from of the queue.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element

    def dequeue(self):
        """
        Remove and return the first element of the queue (FIFO).

        Raise Empty if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        """
        Add an element to the back of the queue.
        """
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

##      NEW CLASS---------------------------- CIRULARLY LINKED LIST
##      NEW CLASS---------------------------- CIRULARLY LINKED LIST

class CircularQueue:
    """
    Queue that uses a cirularly linked list for storage
    """
    class _Node:
        """
        This is a convenient, lightweight nonpublic class for storing a singly linked node.
        The '__slots__'  statically defines the instance attributes.
        """
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    def __iniit__(self):
        """
        Create an empty queue.
        """
        self._tail = None
        self._size = 0

    def __len__(self):
        """
        Return the number of element in the queue.
        """
        return self._size

    def is_empty(self):
        """
        Return True if the queue is empty.
        """
        return self._size == 0

    def first(self):
        """
        Return, but do not remove, the lemenet at the front of the queue.
        
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        return head._element

    def dequeue(self):
        """
        Remove and return the first element of the queue (FIFO).

        Else Raise Empty ecveption.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next        # bypass the old head
        self._size -= 1
        return oldhead._element

    def enqueue(self,e):
        """
        Add an element to the back of the queue.
        """
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest           
        self._tail = newest                     # new node beomes the tail
        self._size += 1

    def rotate(self):
        """
        Rotate front element to the back of the queue.
        """
        if self._size > 0:
            self._tail = self._tail._next       # old head becomes new tail



if __name__ == '__main__':
    airports = CircularQueue()
    
    first = {'name':'BOS'}
    airports.enqueue(first)
    print len(airports)
    print airports.first()['name'] 
    # next
    second = {'name':'ATL'}
    airports.enqueue(second)
    print len(airports)
    print airports.first()['name'] 
    # next
    third = {'name':'MSP'}
    airports.enqueue(third)
    fourth = {'name':'LAX', 'location': 'Los Angeles'}
    airports.enqueue(fourth)
    #print len(airports)
    #print airports.top()['name'] 
    ## next
    #print(airports.pop())
    # next
    while len(airports):
        print(len(airports))
        try:
            if airports.first()['location']:
                print(airports.first()['location'])
        except Exception as e:
            pass
        print(airports.dequeue()['name'])
    print('is the queue empty? ', airports.is_empty())
    
    airports = CircularQueue()
    airports.enqueue('first')
    
    #if __name__ == '__main__':
    #    cqueue = CircularQueue()
    #    cqueue.enqueue('first')
    #    print('print', cqueue.first())
