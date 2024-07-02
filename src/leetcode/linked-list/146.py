class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.previous = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.m = {}
        self.head = Node(0, 0)  # Dummy node pointer to track the head of the list
        self.tail = Node(0, 0)  # Dummy node pointer to track the tail of the list
        self.head.next = self.tail
        self.tail.previous = self.head

    # Appends a new Node to the tail of the list
    def insert(self, node: Node):
        nextNode = self.tail
        previousNode = self.tail.previous

        # Attach the next node
        nextNode.previous = node

        # Attach the new Node to the tail of the list
        node.next = nextNode
        node.previous = previousNode

        # Reconnect the previous Node
        previousNode.next = node

    # Ejects a Node from the list
    def eject(self, node):
        nextNode = node.next
        previousNode = node.previous

        previousNode.next = nextNode
        nextNode.previous = previousNode

    def get(self, key: int) -> int:
        if key in self.m:
            # Eject the Node and insert it at the tail of the list as the most recently used
            self.eject(self.m[key])
            self.insert(self.m[key])
            return self.m[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self.eject(self.m[key])  # Remove the existing Node
        self.m[key] = Node(key, value)  # Add the new node to the map
        self.insert(self.m[key])  # Insert the Node at the tail of the list as the most recently used

        # Remove all references to the oldest Node at the head of the list
        if len(self.m) > self.capacity:
            oldestNode = self.head.next
            self.eject(oldestNode)
            del self.m[oldestNode.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
