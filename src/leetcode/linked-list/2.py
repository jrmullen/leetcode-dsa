# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        overflow = 0

        while l1 or l2 or overflow:
            total = 0
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            total = total + overflow
            overflow = total // 10  # Re-evaluate the overflow value
            total = total % 10  # Drop the leading value if total > 10

            # Add the new node and increment the pointer
            tail.next = ListNode(total)
            tail = tail.next

        return dummy.next
