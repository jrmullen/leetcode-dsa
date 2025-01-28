class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        result = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        
        def dfs(row, col, visited):
            # Mark the current cell as visited
            visited.add((row, col))
            
            total = 0 # Track the total number of fish available in each neighboring cell

            # Visit each neighboring tile
            for dx, dy in directions:
                newRow = row + dx
                newCol = col + dy
                # Stay within the bounds of the grid, do not visit land tiles, and do not re-visited previously visited cells
                if (newRow >= 0 and newCol >= 0
                    and newRow < ROWS and newCol < COLS
                    and grid[newRow][newCol] > 0
                    and (newRow, newCol) not in visited
                ):
                    total += dfs(newRow, newCol, visited)
            
            # Return the `total` number of fish from neighboring cells, plus the number of fish in the current cell
            return total + grid[row][col]
        

        # Traverse the `grid` and DFS starting from every unvisited non-land tile
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] > 0 and (row, col) not in visited:
                    # Update the `result` to be the largest value encountered
                    result = max(result, dfs(row, col, visited))

        return result
