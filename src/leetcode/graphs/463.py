class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        result = 0 # Track the perimeter as the island is explored
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set() # Containing tuples (row, col)
        q = deque()

        # Search the grid until a land tile is found
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    q.append((row, col)) # Add the land tile to the queue
                    visited.add((row, col)) # Mark the tile as visited since it will be the starting point
                    break
        
        # BFS starting at the land tile
        while q:
            # Process everything currently on the queue
            for _ in range(len(q)):
                row, col = q.pop()
                perimeter = 0 # Track the number of sides of the tile that make up the perimeter of the island

                # Visit each neighboring tile
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    neighbor = (row + dr, col + dc)

                    # Any edges bordering the edge of the grid or water tiles will be added to the perimeter
                    if new_row < 0 or new_col < 0 or new_row == ROWS or new_col == COLS or grid[new_row][new_col] == 0:
                        perimeter += 1
                        continue

                    # Add any unvisited neighboring land tiles to the queue
                    if grid[new_row][new_col] == 1 and neighbor not in visited:
                        q.appendleft(neighbor) # Add the neighbor to the queue
                        visited.add(neighbor) # Mark the neighbor as visited to avoid cycles

                # Add the `perimeter` to the total `result` count
                result += perimeter
        
        return result
