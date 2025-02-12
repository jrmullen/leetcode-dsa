class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        # Sort the coins in ascending order
        coins.sort()

        # Build the 2D `dp` aray.
        # The x-axis will be the values from 0 to `amount`
        # The y-axis will be values 0 to len(coins), representing the index of each coin in the `coins` list
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        
        # Populate the values of the `amount` column at index 0 with the base case value of 1.
        # There is only 1 possible way to get a value of 0
        for i in range(n + 1):
            dp[i][0] = 1
        
        # Bottom-up: Starting from the bottom-left corner, working 1 row at a time, bottom to top
        # In order to prevent duplicate combinations, only consider the current coin or coins with larger values.
        # Never choose a smaller coin value

        for i in range(n - 1, -1, -1): # Starting at the bottom row and working up
            for a in range(amount + 1): # For each `amount` value column
                # If the current amount `a` is larger than the current coin's value, a combination can be made
                if a >= coins[i]:
                    # Consider using a larger coin - look down 1 row 
                    dp[i][a] += dp[i + 1][a]
                    # Consider using the current coin value. subtract the coin value and see how many combinations can be made
                    # with the remaining total
                    dp[i][a] += dp[i][a - coins[i]] 

        # Finally, return the total number
        return dp[0][amount]
