class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        longest = 0
        nums = sorted(set(nums)) # sort the input `nums` and convert to a set to remove duplicate values
        dp = {n: 1 for n in nums} # Pre-populate a dict for each value in `nums` with a default value of `1`

        for num in nums:
            square = num ** 2 # Calculate the square of `num`
            length = 1
            # If the `square` exists in the `dp` dict update the length and update the length of the square in `dp`
            if square in dp:
                length = 1 + dp[num]
                dp[square] = length

            # Update the `longest` with the largest encountered value
            if length > longest:
                longest = length 
        
        return longest if longest > 1 else -1
