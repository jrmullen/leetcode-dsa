class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        maxWidth = 0
        stack = []

        # Populate the stack with values in increasing order
        for index, num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:
                stack.append(index) # Add the index of the value to the stack

        # Iterate over `nums` in reverse order
        for j in range(len(nums) - 1, -1, -1):
            # If the number is greater than the value at the top of the stack, calculate the width and pop the top value
            while stack and nums[stack[-1]] <= nums[j]:
                maxWidth = max(maxWidth, j - stack.pop())
                
        return maxWidth
