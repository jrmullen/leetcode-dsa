class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        # Build the DP list, defaulting to -INF so max() always overwrites it
        # The `dp` list represents the maximum possible score Alice can get for each position
        dp = [float('-inf')] * (n + 1)
        dp[-1] = 0 # Set the last (extra) element to 0 to account for the base case of having no stones left to choose from

        # Top-down approach: start at the end of the `stoneValue` list and work backwords tracking the best possible move
        for i in range(n - 1, -1, -1):
            # From each starting position `i`, consider the 3 possible moves.
            # The stones at position `i`, `i + 1`, and `i + 2` are up for grabs
            score = 0
            for j in range(i, i + 3):
                # Stay within bounds. Do not allow `j` to exceed the size of the list.
                if j >= n:
                    break
                
                # Increment the `score` to account for the possible move and calculate the outcome of that move
                # Keep the most beneficial move and store it in the `dp` list
                score += stoneValue[j]
                dp[i] = max(dp[i], score - dp[j + 1])
        
        # After working backwards and determining the best move at each step, if the first move is 0 there is a tie.
        # If the first move has a negative value, Alice will lose. If the first move has a positive value Alice will win.       
        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'
