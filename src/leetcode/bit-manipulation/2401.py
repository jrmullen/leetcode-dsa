class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        result = 0
        used = 0
        l = 0

        for r in range(len(nums)):
            # If the new number ANDed with the currently `used` bits is non-zero, shrink the window until it is valid
            while used & nums[r] != 0:
                used ^= nums[l] # Un-set the `used` bits by XORing with the current left pointer
                l += 1 # Move the left pointer forward to shrink the window
            
            used |= nums[r] # Add the new number's bits to the `used` bits by ORing them together
            result = max(result, (r - l) + 1) # Track the largest window (subarray) encountered

        return result
