class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        currentSum = 0

        for num in nums:
            # If the `currentSum` ever dips below 0, reset it back to 0
            if currentSum < 0:
                currentSum = 0
            
            # Add `num` the `currentSum`
            currentSum += num

            # Compare the `currentSum` to the maximum subarray sum `result` and keep the largest value
            result = max(result, currentSum)
        
        # Return the largest subarray sum
        return result
