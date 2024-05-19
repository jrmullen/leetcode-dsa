class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        slow2 = 0

        while True:
            fast = nums[fast] 
            fast = nums[fast] # Move the fast pointer twice
            slow = nums[slow] # Move the slow pointer once

            # When the pointers cross the first intersection point has been found
            if fast == slow:
                break
        
        while True:
            # Move both slow pointers forward once
            slow = nums[slow]
            slow2 = nums[slow2]

            # When the pointers cross we have found the repeated number
            if slow == slow2:
                return slow2
