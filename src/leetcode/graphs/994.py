class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        result = 0
        rows = len(grid)
        columns = len(grid[0])
        q = deque()
        freshCount = 0
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        # Traverse the entire grid
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 2:
                    q.appendleft((r, c))  # Add the rotten oranges to the initial queue
                if grid[r][c] == 1:
                    freshCount += 1  # Count the number of fresh oranges we initially start with

        # Important to include a check on `freshCount` > 0 to avoid unnecessary iterations
        while q and freshCount > 0:

            # Multi-source BFS - process all currently rotten oranges before progressing to the next "batch"
            for _ in range(len(q)):
                r, c = q.pop()

                for rowDir, colDir in directions:
                    row = r + rowDir
                    col = c + colDir

                    # If the tile is within the bounds of the grid and is a fresh orange
                    if row in range(rows) and col in range(columns) and grid[row][col] == 1:
                        grid[row][col] = 2  # Mark as rotten
                        freshCount -= 1  # Decrement the count of fresh oranges
                        q.appendleft((row, col))  # Append to the queue for the next iteration of BFS

            # Progress the time count
            result += 1

        return result if freshCount == 0 else -1
