class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        result = 0
        # Space-optimized - keep a running sum of the `left` and `right` halves of the split
        left = 0
        right = 0
        
        # Pre-calculate the total sum
        for num in nums:
            right += num
        
        for i in range(len(nums) - 1): # Do not include the last element
            # Increase the `left` sum, and decrease the `right` sum
            left += nums[i]
            right -= nums[i]

            # Increment the the `result` counter to include any valid splits
            if left >= right:
                result += 1
        
        return result
