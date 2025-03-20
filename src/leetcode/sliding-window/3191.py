class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = 0
        l = 0

        # Iterate over the list, considering a window of 3 values. Immediately flip any 0s encountered
        # to avoid leaving stragglers behind
        for i in range(len(nums) - 2):
            # If the leftmost value is a 0, flip the window
            if nums[i] == 0:
                # Flip
                for j in range(i, i + 3) # Window of 3 elements
                    nums[j] ^= 1 # XOR to flip the value
                result += 1 # Increment the counter
        
        # If either of the last 2 elements are still a 0 at the end, the list is invalid
        if nums[-1] == 0 or nums[-2] == 0:
            return -1
        else:
            return result
