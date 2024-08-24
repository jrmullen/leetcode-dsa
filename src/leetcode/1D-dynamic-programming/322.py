class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Bottom-up approach:
        # Calculate the minimum counts for integers 1 to `amount` by using the largest coin available
        # and pulling the value of the difference from the `dp` list

        # Sort the `coins` list into ascending order
        coins.sort()
        
        # Populate `dp` with default values
        dp = [float('inf')] * (amount + 1) # `amount + 1` to include 0 as a base case
        dp[0] = 0 # Base case - it takes 0 coins to sum to 0

        # Calculate the minimum number of coins for every number from 1 to `amount`
        for i in range(1, amount + 1):
            # The minimum number of coins will be the largest coin possible + the minimum coins required
            # to reach whatever difference is left over. That value can be pulled from `dp`, which contains the
            # minimum number of coins to reach eat amount `i`
            for coin in coins:
                difference = i - coin
                if difference < 0:
                    break # Stop iterating once a coin that is too large to go into the amount `i` is found

                # If a `difference` was able to be calculated, the value is `dp[difference]` +1 to accoint for the new coin.
                # Otherwise, default to Infinity to signify that the amount was not able to be calculated
                dp[i] = min(dp[i], dp[difference] + 1)

        # If the amount was not able to be calculated it will still have the default value of Infinity
        if dp[amount] < float('inf'):
            return dp[amount]
        else:
            return -1
