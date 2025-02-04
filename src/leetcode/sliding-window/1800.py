class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = nums[0] # Track the largest sum encountered
        total = nums[0] # Track the sum of the current subarray window

        for i in range(1, len(nums)):
            # If the numbers are ascending, add the number to the `total` window sum
            if nums[i] > nums[i - 1]:
                total += nums[i]
                result = max(result, total) # Update the `result` with the largest sum
            else:
                total = nums[i] # Reset the `total` window sum
        
        return result
