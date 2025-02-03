class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)] # Build the DP matrix with 1 extra row/col
        dp[1][1] = 1 # Pre-populate the starting point as the base case
        
        # Iterate over each row from left to right, skipping the first row/col as not to include "buffer" values
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                # Base case: the starting point has already been populated
                if row == 1 and col == 1:
                    continue
                
                # The number of moves for a tile is the number of moves from the tile to the left + the number of moves from the tile above
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        # Return the value assigned to the ending tile
        return dp[m][n]
