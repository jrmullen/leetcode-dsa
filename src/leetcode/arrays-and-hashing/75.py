class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0 # Left pointer will track where the rightmost 0 should be placed
        m = 0 # Middle pointer will traverse the list until it meets the right pointer
        r = len(nums) - 1 # Right pointer will track where the leftmost 2 should be placed

        while m <= r:
            if nums[m] == 0: # Swap values with the left pointer
                nums[m], nums[l] = nums[l], nums[m]
                l += 1 # Move the pointer forward
            elif nums[m] == 2: # Swap values with the right pointer
                 nums[m], nums[r] = nums[r], nums[m]
                 r -= 1 # Move the pointer forward
                 continue # IMPORTANT: do not move the middle pointer forward so the index is re-processed
            m += 1 # Move the middle pointer forward
        
        return nums
