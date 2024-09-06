# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert `nums` to a set for efficiently looking up existence of values
        nums = set(nums)

        # Remove the head node until its value is no longer a number in `nums`
        while head and head.val in nums:
            head = head.next
        
        # If all nodes have been removed, return `None`
        if not head:
            return None
        
        # Snapshot the existing `head`
        currentNode = head

        # Traverse the remaining nodes, and remove the ones that contain numbers in `nums`
        while currentNode.next:
            if currentNode.next.val in nums:
                currentNode.next = currentNode.next.next
            else:
                currentNode = currentNode.next
        
        # Return the modified `head` that should now only contain values that are not in `nums`
        return head
