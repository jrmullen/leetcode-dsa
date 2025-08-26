class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) # Right pointer dual purpose tracking the size of the array

        while l < r:
            if nums[l] == val:
                nums[l] = nums[r - 1] # Overwrite the left value with the right value
                r -= 1 # Shift the right pointer
            else:
                l += 1 # Move the left pointer forward

        return r
