# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Start with an empty dummy node to avoid edge cases
        tail = dummy

        # There are both an L1 and L2 node available to compare
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            # Progress the tail
            tail = tail.next

        # L1 has an available node, but L2 does not, add the rest of the L1 list to the tail
        if list1:
            tail.next = list1

        # # L2 has an available node, but L1 does not - addd the rest of the L2 list to the tail
        if list2:
            tail.next = list2

        return dummy.next
