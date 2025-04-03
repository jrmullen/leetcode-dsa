class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float('INF')
        l = 0 # Left pointer begins at 0
        total = 0 # Total starts as 0

        # Sliding window: move the right pointer across the list of `nums`
        for r in range(len(nums)):
            total += nums[r] # Add the new number to the `total` count

            # If the `target` has been exceeded, update the `result` with the smallest window size found
            while total >= target and l <= r:
                # Update the result with the shortest window with a sum exceeding the `target`
                if total >= target:
                    result = min(result, (r - l) + 1)

                # Shrink the window until its sum no longer exceeds the target
                total -= nums[l] # Remove the left number's value from the `total` sum
                l += 1 # Move the left pointer forward
                    
        # If no value window was found, return the default value of 0
        return result if result != float('INF') else 0
