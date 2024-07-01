class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        visited = set()
        result = 0

        if not grid:
            return 0

        def dfs(row, column):
            # Base case - if the tile is out of bounds, is a water tile, or has been visited
            if (row not in range(rows)
                    or column not in range(columns)
                    or grid[row][column] == 0
                    or (row, column) in visited):
                return 0

            # Mark the tile as visited
            visited.add((row, column))

            # DFS each adjacent tile
            return 1 + dfs(row + 1, column) + dfs(row - 1, column) + dfs(row, column + 1) + dfs(row, column - 1)

        # Loop over each tile in the grid and run a DFS on any unvisited island tiles to find the size of the island
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1 and (r, c) not in visited:
                    result = max(result, dfs(r, c))

        return result
