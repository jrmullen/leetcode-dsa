class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # Two pointers
        l, r = 0, 1
        
        # Iterate over the list of `nums` in pairs, comparing the parity
        while r < len(nums):
            # Base case: if the pair have the same parity, the array is no longer special
            if nums[l] % 2 == nums[r] % 2:
                return False

            # Shift the window forward
            l += 1
            r += 1
        
        return True
