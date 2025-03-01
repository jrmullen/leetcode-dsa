class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        stack = []

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                # Multiply the `i`th element by 2
                nums[i] *= 2

                # Set the `i + 1`th element to 0
                nums[i + 1] = 0
            
            # If the value is non-zero add it to the stack
            if nums[i] != 0:
                stack.append(nums[i])

        # Account for the last element
        if nums[-1] != 0:
            stack.append(nums[-1])
        
        while len(stack) < len(nums):
            stack.append(0)

        return stack
