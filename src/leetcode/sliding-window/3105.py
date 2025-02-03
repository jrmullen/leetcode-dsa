class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        l = 0

        # First pass - left to right to find the longest increasing subarray
        for r in range(n):
            # If the window is larger than 1 element and the array is no longer increasing
            if (r - l) + 1 > 1 and nums[r - 1] >= nums[r]:
                # Move the left pointer forward to reset the window
                l = r
                continue
            result = max(result, (r - l ) + 1)
        
        # Second pass - right to left to find the longest decreasing subarray
        r = n - 1
        for l in range(n - 1, -1, -1):
            # If the window is larger than 1 element and the array is no longer decreasing
            if (r - l) + 1 > 1 and nums[l] <= nums[l + 1]:
                # Move the right pointer forward to reset the window
                r = l
                continue
            result = max(result, (r - l ) + 1)
        
        return result
