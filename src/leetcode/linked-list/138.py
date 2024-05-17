"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0, None, None)
        tail = dummy
        nodesMap = {}

        while head:
            # If the node has already been created, do not create a new one
            if head in nodesMap:
                newNode = nodesMap[head]
            else:
                nodesMap[head] = Node(head.val)
                newNode = nodesMap[head]

            # If the random node has already been created, do not create a new one
            if head.random in nodesMap:
                newNode.random = nodesMap[head.random]
            else:
                if head.random is not None:
                    nodesMap[head.random] = Node(head.random.val)
                    newNode.random = nodesMap[head.random]

            # Attach the new node to the tail of the list and increment pointers
            tail.next = newNode
            tail = tail.next
            head = head.next

        return dummy.next
