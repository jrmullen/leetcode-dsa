class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()
        visited = set()

        # Traverse the `grid` until the starting location is found
        found = False
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '*':
                    # Add the starting tile to the `q`
                    q.appendleft((row, col, 0)) # (row, col, distance)
                    found = True
                    break
            if found:
                break
        
        # BFS to find the closest food tile
        while q:
            row, col, distance = q.pop()

            # Do not re-visit previously visited tiles
            if (row, col) in visited:
                continue
            
            # Mark the tile as visited
            visited.add((row, col))

            # If the tile is a food tile, return the distance
            if grid[row][col] == '#':
                return distance
            
            # Visit all neighboring tiles
            for dx, dy in directions:
                newRow = row + dx
                newCol = col + dy

                # Stay within the bounds of the tiles, do not re-visit tiles, and ignore obstacles
                if (
                    newRow >= 0 and newCol >= 0 and
                    newRow < ROWS and newCol < COLS and
                    (newRow, newCol) not in visited and
                    grid[newRow][newCol] != 'X'
                ):
                    q.appendleft((newRow, newCol, distance + 1))
        
        # If there are no moves left and food still has not been found, return the default value
        return -1
