# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = head
        
        while head.next:
            # Snapshot nodes to compare
            leftNode = head.val
            rightNode = head.next.val

            # Calculate GCD
            # Euclidean algorithm: The GCD is the largest number that divides two numbers without a remainder
            while (rightNode != 0):
                # With `leftNode` as the larger number, once the remainder of `leftNode % rightNode` is 0,
                # `leftNode` will be the GCD 
                leftNode, rightNode = rightNode, leftNode % rightNode

            # Insert new node for GCD
            gcdNode = ListNode(leftNode, head.next)
            head.next = gcdNode

            # Move head forward 2 nodes
            head = head.next.next

        return dummyNode
