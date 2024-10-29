class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        result = 0
        dp = [[-1 for _ in range(COLS)] for _ in range(ROWS)]
        directions = [(-1, 1), (0, 1), (1, 1)]

        def dfs(row, col, dp):
            # If the maximum value is memoized, return it immediately
            if dp[row][col] != -1:
                return dp[row][col]
            
            # Visit each cell in the allowed directions
            maximum = 0
            for (x, y) in directions:
                newRow = row + x
                newCol = col + y

                # If the next cell is within the bounds of the grid and is larger than the current cell's value
                if 0 <= newRow < ROWS and 0 <= newCol < COLS and grid[row][col] < grid[newRow][newCol]:
                    maximum = max(maximum, 1 + dfs(newRow, newCol, dp))
            
            # Save the value to the memoized `dp` and return the maximum
            dp[row][col] = maximum
            return maximum


        # Start at each cell in the first column of the grid
        for row in range(ROWS):
                result = max(result, dfs(row, 0, dp)) # DFS from each cell and keep the largest value
        return result
