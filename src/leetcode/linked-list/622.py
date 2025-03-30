class ListNode:

    def __init__(self, val, next = None):
        self.val = val
        self.next = next


class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.max_size = k
        self.tail = None
        self.head = None

    def enQueue(self, value: int) -> bool:
        if self.size == self.max_size:
            return False

        node = ListNode(value, self.head) # Create the new node

        # If the queue is empty, set the new `node` as both the head and tail nodes
        if self.size == 0:
            self.head = node # Point to the new node
            self.tail = node
        else: # Otherwise, insert the new `node` as the head node
            self.head.next = node # Point the previous head node to the new head
            self.head = node # Reassign the head pointer
        self.size += 1 # Update the `size` counter
        return  True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        
        save = self.tail # Temporarily snapshot the tail node
        self.tail = self.tail.next # Reassign the tail pointer
        save.next = None # Sever tail node completely for GC
        self.size -= 1 # Update the `size` counter
        return True

    def Front(self) -> int:
        return -1 if self.size == 0 else self.tail.val

    def Rear(self) -> int:
        return -1 if self.size == 0 else self.head.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
