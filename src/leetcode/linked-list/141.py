# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # Progress the fast pointer twice as fast
        while fast:
            fast = fast.next
            if fast:
                slow = slow.next
                fast = fast.next

            # If the pointers ever cross there is a cycle in the list
            if slow == fast:
                return True
        return False
