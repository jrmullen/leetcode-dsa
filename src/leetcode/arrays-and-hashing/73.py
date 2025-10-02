class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])

        # Track which rows/columns have been seen containing a 0
        rows_seen = set()
        cols_seen = set()

        # Iterate over the matrix once to record all of the rows and columns containing zeros
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    rows_seen.add(row)
                    cols_seen.add(col)
        
        # Iterate once more to backfill all affected rows
        for row in range(ROWS):
            for col in range(COLS):
                # If either the row or the column have been seen as 0, update the cell to be a 0
                if row in rows_seen or col in cols_seen:
                    matrix[row][col] = 0
        
        return matrix # Return the modified matrix
