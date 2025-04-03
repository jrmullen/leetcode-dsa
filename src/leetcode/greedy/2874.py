class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result = float('-INF') # Track the largest value calculated

        # Intuition: to maximize the result of the equation, maximize `i` and `k`, while minimizing `j`
        max_i = nums[0] # Track the largest value encountered as `i`
        max_difference = 0 # Tracking the minimum `j` that occurs after `i` is difficult, so instead track the maximum difference `i - j`

        # To simplify guaranteeing `i` and `j` come before `k`, iterate over each number in the list of `nums` as `k`
        for k in nums:
            result = max(result, max_difference * k) # First, calculate the value of the current triplet using the `max_difference`
            max_i = max(max_i, k) # Next, compare `k` with the current `i` and update if necessary
            max_difference = max(max_difference, max_i - k) # Finally, see if `k` is a new minimum `j`, maximizing the `max_difference`
        
        # If the `result` is negative, default to a value of 0
        return max(result, 0)
