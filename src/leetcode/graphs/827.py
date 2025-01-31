class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        result = 0
        islandMap = {} # (x, y): island -- Maps a coordinate in the grid to the island in which it belongs
        sizes = defaultdict(int) # island: size -- maps an island to an integer representing its size
        islandCount = 0 # Counter used to assign each newly visited island a unique integer ID

        def dfs(row, col, island):
            # Base case: The tile is out of bounds, is a water tile, or has already been visited
            if (
                row < 0 or col < 0
                or row == ROWS or col == COLS
                or (row, col) in islandMap
                or grid[row][col] == 0
            ):
                return
            
            # Map the tile to it's island, and increase the island size counter to include the new tile
            islandMap[(row, col)] = island
            sizes[island] += 1
            
            # Finally, visit each neighboring tile
            for dx, dy in directions:
                dfs(row + dx, col + dy, island)

        # First, DFS from each tile in the `grid` to map out the islands and their sizes
        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, islandCount)
                islandCount += 1

        # Finally, iterate over the `grid` and sum up the size of all unique adjacent islands
        for row in range(ROWS):
            for col in range(COLS):
                # If the tile is already a part of an island, nothing changes so return the size of the island
                if (row, col) in islandMap:
                    result = max(result, sizes[islandMap[(row, col)]])
                    continue

                # Sum the size of all distinct islands touching the cell
                total = 1 # The island size starts at 1 to account for the "flipped" tile
                visited = set()
                for dx, dy in directions:
                    newRow = row + dx
                    newCol = col + dy
                    # If the neighboring tile is not in the `islandMap`, skip it
                    if (newRow, newCol) not in islandMap:
                        continue
                    
                    # If the `currentIsland` has already been included in the `total` count, skip it
                    currentIsland = islandMap[(newRow, newCol)]
                    if currentIsland in visited:
                        continue

                    # Add the `currentIsland`'s size to the `total` count and mark the island as visited
                    total += sizes[currentIsland]
                    visited.add(currentIsland)
                
                # Update the `result` with the largest `total` encountered
                result = max(result, total)

        return result
