# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Insert a dummy note to avoid edge cases
        dummy = ListNode()
        dummy.next = head

        # Count the number of nodes we have traversed
        count = 0

        left = dummy
        right = dummy

        # Move the right pointer forward until it hits the end
        while right:
            right = right.next
            if count > n: # Only move the left pointer forward once the gap has been established
                left = left.next
            count += 1

        # Drop the Nth node, and instead point to node N+1
        left.next = left.next.next

        return dummy.next
