class Node:
    def __init__(self, value, next=None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

class MyCircularDeque:
    def __init__(self, k: int):
        self.maxLength = k
        self.length = 0
        self.head = None
        self.tail = None

    def insertFront(self, value: int) -> bool:
        if self.isFull(): # If the queue is full, return False
            return False
        
        if not self.head: # If the queue is empty create a new node
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
            self.length += 1
            return True

        # Otherwise, insert a new node at the front of the queue and increase the length
        newNode = Node(value, None, self.head)
        self.head.next = newNode
        self.head = self.head.next
        self.length += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull(): # If the queue is full, return False
            return False
        
        if not self.tail: # If the queue is empty create a new node
            newNode = Node(value)
            self.tail = newNode
            self.head = newNode
            self.length += 1
            return True
        
        # Otherwise, insert a new node at the end of the queue  and increase the length
        newNode = Node(value, self.tail, None)
        self.tail.prev = newNode
        self.tail = self.tail.prev
        self.length += 1
        return True

    def deleteFront(self) -> bool:
        if not self.head: # If the queue is empty return False
            return False
        
        if self.length == 1: # If the queue only has 1 Node remove it
            self.head = None
            self.tail = None
            self.length -= 1
        else: # Otherwise remove the head node from the queue
            self.head = self.head.prev
            self.head.next.prev = None
            self.head.next = None
            self.length -= 1
        return True

    def deleteLast(self) -> bool:
        if not self.tail: # If the queue is empty return False
            return False
        
        if self.length == 1: # If the queue only has 1 Node remove it
            self.head = None
            self.tail = None
            self.length -= 1
        else: # Otherwise remove the tail node from the queue
            self.tail = self.tail.next
            self.tail.prev.next = None
            self.tail.prev = None
            self.length -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.head.value

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.tail.value

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.maxLength


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
