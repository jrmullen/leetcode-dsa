class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        result = []

        # Calculate the remainder of the sum dividided by `p`. This will be the target sum of the `result` subarray
        remainder = sum(nums) % p

        # If the `remainder` is 0, nothing needs to be removed
        if remainder == 0:
            return 0

        # Map the remainder of prefix sums to their last index in `nums`
        modMap = { 0: -1 }

        currentSum = 0 # Track the running sum
        minLength = len(nums) # Track the minimum length subarray

        for i, n in enumerate(nums):
            # Update the running total
            currentSum = (currentSum + n) % p
            
            # `currentSum - prefix = remainder` => `prefix = currentSum - remainder`
            # Can result in negatives, so add `p` to get a positive result
            prefix = (currentSum - remainder + p) % p

            # If the prefix already exists in the map, update `minLength` to be the length of the smallest subarray
            if prefix in modMap:
                minLength = min(minLength, i - modMap[prefix])
            
            # Store the last index of the prefix sum in the map
            modMap[currentSum] = i
    
        return -1 if minLength == len(nums) else minLength
