class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1) # Bottom-up tabulation: store the number of possible combinations for each number from 0 to `target`
        dp[0] = 1 # 1 way to make 0

        # Iterate over each number from 1 to `target`
        for i in range(1, target + 1):
            # Any number from the list may be chosen when creating combinations, so iterate over the entire list of `nums` each time
            for num in nums:
                difference = i - num # Calculate the difference between the total `i` and the current `num`
                if difference >= 0: # If the diference is < 0 it does not need to be considered
                    dp[i] += dp[difference] # Update the count of combinations in the `dp` array with the value saved for the `difference`

        # The final value in the `dp` array for the `target` value will be the total number of possible combinations
        return dp[target]
