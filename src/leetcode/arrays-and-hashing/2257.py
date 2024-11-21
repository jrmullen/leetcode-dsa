class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Grid:
        # 0 - open & unguarded
        # 1 - guarded
        # 2 - blocking tile (wall or guard)
        grid = [[0 for _ in range(n)] for _ in range(m)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        result = 0 

        # Populate the grid with all of the `walls`
        for row, col in walls:
            grid[row][col] = 2
        
        # Populate the grid with all of the `guards`
        for row, col in guards:
            grid[row][col] = 2

        def dfs(row, col, direction):
            # Base case: the tile is a blocking entity (guard or wall) or outside the bounds of the grid
            if row < 0 or row > m - 1 or col < 0 or col > n - 1 or grid[row][col] == 2:
                return
            
            # Mark the tile as guarded
            grid[row][col] = 1

            # Check the next tile in the `direction` until the base case is hit
            x, y = direction
            dfs(row + x, col + y, direction)
        
        # DFS from each guard tile to mark all guarded tiles
        for row, col in guards:
            for x, y in directions:
                dfs(row + x, col + y, [x, y])
        
        # Count & return the number of remaining unguarded (value `0`) cells
        return sum(row.count(0) for row in grid)
