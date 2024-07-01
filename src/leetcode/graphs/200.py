class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        columns = len(grid[0])
        visited = set()
        result = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, column = q.popleft()

                directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
                for dRow, dCol in directions:
                    r = row + dRow
                    c = column + dCol

                    # If the adjecent value is within the bounds of the board, is not a water tile, and has not been visited
                    if r in range(rows) and c in range(columns) and grid[r][c] == "1" and (r, c) not in visited:
                        q.append((r, c))
                        # Mark the tile as visited
                        visited.add((r, c))

        # Iterate over each tile in the grid
        for c in range(columns):
            for r in range(rows):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)

                    # The BFS should mark all adjacent island tiles as visited,
                    # so if BFS is run again it should be a completely new island
                    result += 1

        return result
