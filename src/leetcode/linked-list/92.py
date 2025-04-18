# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # Create a new dummy node at the front of the linked list
        prev = dummy # Track the previous node. Starts at the `dummy` node
        current = head # Track the current node. Starts at the `head` of the linked list

        # Traverse the linked list until the `left` node is reached
        for _ in range(left - 1):
            prev = current
            current = current.next
        
        front = prev # Snapshot the node before the `left` node
        left_node = current # Snapshot the node in the `left` position
        prev = None # Sever the `prev` pointer

        # Reverse the nodes between `left` and `right`
        for _ in range(right - left + 1):
            nxt = current.next # Snapshot the next node
            current.next = prev # Reverse the connection by pointing to the previous node
            prev = current # Update the `prev` pointer
            current = nxt # Update the `current` pointer

        # Finally, re-attach the reversed portion of the linked list to the front of the list
        # When the above loop is completed the `current` node will be pointing to the node after the `right` node
        # and the `prev` node will be the start of the reversed portion of the linked list
        front.next.next = current # `current` will be the start of the last chunk of nodes. Add it to the end of the list
        front.next = prev # `prev` will be the start of the reversed nodes. Add it between the start and end chunks

        # The head will be the node the dummy node is pointing to
        return dummy.next
