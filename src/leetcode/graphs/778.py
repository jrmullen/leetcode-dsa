class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid) # Grid is N x N
        
        result = 0
        heap = [(grid[0][0], 0, 0)] # (height, x, y) - starting at point 0, 0
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Dijkstra's algorithm, tracking the largest height encountered
        while heap:
            elevation, x, y = heapq.heappop(heap)

            # Do not re-visit previously visited tiles
            if (x, y) in visited:
                continue
            
            # Mark the tile as visited
            visited.add((x, y))

            # Update the `result` to account for the elevation of the current tile
            result = max(result, elevation)

            # If the bottom-right tile has been reached, return the `result` counter
            if x == N - 1 and y == N - 1:
                return result

            # Visit each neighboring tile
            for dx, dy in directions:
                row = x + dx
                col = y + dy
                # If the neighboring tile is within the bounds of the grid and has not yet been visited, push it onto the heap
                if row >= 0 and row < N and col >= 0 and col < N and (row, col) not in visited:
                    heapq.heappush(heap, (grid[row][col], row, col))
            
        return result
