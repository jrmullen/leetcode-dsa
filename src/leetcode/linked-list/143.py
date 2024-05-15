# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # If the list is empty or contains a single node, there is nothing to be done
        if head is None or head.next is None:
            return

        # Split the list into 2 halves
        slow = head
        fast = head.next

        # Move `fast` forward 2 nodes at a time
        while fast:
            fast = fast.next
            if fast:
                slow = slow.next
                fast = fast.next

        # When `fast` hits the end of the list, `slow` will be right before the midpoint
        first_half = head
        second_half = slow.next
        slow.next = None  # Break the link so we are left with 2 independent halves

        # Reverse the second half of the list
        current = second_half
        previous = None  # The head of the reversed `second_half` list
        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt

        # Overwrite `second_half` to be the reversed list
        second_half = previous

        # Merge the 2 lists back together
        while second_half:
            # Save a pointer to the next value of each half so we can safely break the links
            nxt1 = first_half.next
            nxt2 = second_half.next

            # Insert the node from `second_half` between the `first_half` node and `first_half.next`
            first_half.next = second_half
            second_half.next = nxt1

            # Shift pointers
            first_half = nxt1
            second_half = nxt2
