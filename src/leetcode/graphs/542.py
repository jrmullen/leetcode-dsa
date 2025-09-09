class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        q = deque() # (row, col) tuples

        for row in range(ROWS):
            for col in range(COLS):
                if mat[row][col] == 0: # Push all 0's onto the queue
                    q.appendleft((row, col))
                else: # Otherwise, overwrite with an arbitrary large value
                    mat[row][col] = float('INF')

        # Multi-source BFS starting at 0's working outward
        while q:
            row, col = q.pop()

            # Visit each neighboring tile
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = row + dx, col + dy

                # If the neighboring tile is within the bounds of the matrix and has a value greater than the current distance, overwrite
                if 0 <= nr < ROWS and 0 <= nc < COLS and mat[nr][nc] > mat[row][col] + 1:
                    mat[nr][nc] = mat[row][col] + 1
                    q.appendleft((nr, nc)) # Push the new cell onto the queue

        return mat
