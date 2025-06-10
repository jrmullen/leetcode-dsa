class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1 # Index 0 will always be the smallest number, so start at index 1

        # Iterate over each element starting at index 1
        for r in range(1, len(nums)):
            # If the right value is larger than the value before the left pointer, swap them
            if nums[r] > nums[l - 1]:
                nums[l], nums[r] = nums[r], nums[l] # Swap the values in place
                l += 1 # Move the left pointer forward
        
        return l # The left pointer will end at the index of the last unique number
