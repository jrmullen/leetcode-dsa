class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        result = 0
        M = len(grid)
        N = len(grid[0])

        rows = [0] * M
        cols = [0] * N

        # Pre-compute the number of servers in each row/column
        for row in range(M):
            for col in range(N):
                if grid[row][col] == 1:
                    rows[row] += 1
                    cols[col] += 1

        # Find the servers that communicate
        for row in range(M):
            for col in range(N):
                # If the current tile is a server and its row/column also contains a server, they will communicate
                if grid[row][col] == 1 and (rows[row] > 1 or cols[col] > 1):
                    result += 1

        return result
