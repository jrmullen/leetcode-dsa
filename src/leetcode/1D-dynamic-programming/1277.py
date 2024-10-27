class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        result = 0
        # Memoize result count
        cache = {} # (row, col): count

        def dfs(row, col):
            # Base case: the position is outside the bounds of the matrix or has a value of 0
            if row == ROWS or col == COLS or matrix[row][col] == 0:
                return 0
            
            # # If the count has already been defined for the position, return the cached value
            if (row, col) in cache:
                return cache[(row, col)]

            count = 1 # Since the value must be `1` it will have minimum 1 possible square

            # DFS checking every position left, down, and diagonal. Keep the minimum value
            count += min(
                dfs(row + 1, col),
                dfs(row, col + 1),
                dfs(row + 1, col + 1)
            )
            cache[(row, col)] = count # Memoize the count to avoid duplicate work
            return count
        
        # DFS starting at each position in the matrix
        for r in range(ROWS):
            for c in range(COLS):
                result += dfs(r, c)
        
        return result
