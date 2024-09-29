class Node:
    def __init__(self, freq):
        self.freq = freq
        self.next = None
        self.prev = None
        self.keys = set()


class AllOne:
    def __init__(self):
        self.head = Node(0) # Dummy node
        self.tail = Node(0) # Dummy node
        # Link head and tail nodes to create a doubly linked list
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {} # Key : Node mapping

    # Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1
    def inc(self, key: str) -> None:
        if key in self.map:
            node = self.map[key]
            frequency = node.freq
            node.keys.remove(key) # remove the `key` from the existing node

            nextNode = node.next
            if nextNode == self.tail or nextNode.freq != frequency + 1:
                # If the next node does not exist or does not have the needed frequency, create a new Node
                newNode = Node(frequency + 1)
                newNode.keys.add(key)
                # Update pointers to insert the new Node
                newNode.prev = node
                newNode.next = nextNode
                node.next = newNode
                nextNode.prev = newNode
                self.map[key] = newNode # Update the `map`
            else:
                nextNode.keys.add(key)
                self.map[key] = nextNode # Update the `map`
            
            # If the `node` has no more `keys`, remove it from the Linked List
            if not node.keys:
                self.removeNode(node)
        else:
            firstNode = self.head.next
            # If the list is empty, or the first node in the list has a frequency > 1, create and insert a new node
            if firstNode == self.tail or firstNode.freq > 1:
                newNode = Node(1)
                newNode.keys.add(key)
                # Update pointers to insert the `newNode` as the new first node
                newNode.prev = self.head
                newNode.next = firstNode
                firstNode.prev = newNode
                self.head.next = newNode
                self.map[key] = newNode # Update the `map`
            else:
                firstNode.keys.add(key)
                self.map[key] = firstNode # Update the `map`

        
    # Decrements the count of the string `key` by 1. If the count of `key` is 0 after the decrement, remove it from the data structure.
    # It is guaranteed that `key` exists in the data structure before the decrement.
    def dec(self, key: str) -> None:
        if key not in self.map:
            return  # Key does not exist

        node = self.map[key]
        frequency = node.freq
        node.keys.remove(key) # remove the `key` from the existing node

        # If the frequency of the node is > 1, update to point to the new frequency node
        if node.freq > 1:
            prevNode = node.prev
            if prevNode == self.head or prevNode.freq != frequency - 1:
                # If the previous node does not exist or does not have the needed frequency, create a new Node
                newNode = Node(frequency - 1)
                newNode.keys.add(key)
                # Update pointers to insert the new Node
                newNode.prev = prevNode
                newNode.next = node
                node.prev = newNode
                prevNode.next = newNode
                self.map[key] = newNode # Update the `map`
            else:
                prevNode.keys.add(key)
                self.map[key] = prevNode # Update the `map`
        else: # if the frequency of the node is 1, remove the node
            del self.map[key] # Remove the `key` from the `map`
        
        # If the `node` has no more `keys`, remove it from the Linked List
        if not node.keys:
            self.removeNode(node)

    # Returns one of the keys with the maximal count. If no element exists, return an empty string `""`
    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return '' # The linked list is empty, return default string
        for key in self.tail.prev.keys:
            return key # Return the first `key` in the first Node's `keys` set
        
        
    # Returns one of the keys with the minimum count. If no element exists, return an empty string `""`
    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ''
        for key in self.head.next.keys:
            return key # Return the first `key` in the last Node's `keys` set
    
    def removeNode(self, node):
        # Update pointers to remove the current `node` from the Linked List
        prevNode = node.prev
        nextNext = node.next

        nextNext.prev = prevNode
        prevNode.next = nextNext


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
