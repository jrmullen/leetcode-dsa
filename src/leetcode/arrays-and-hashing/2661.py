class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        ROWS = len(mat)
        COLS = len(mat[0])

        
        rowCount = { i: 0 for i in range(ROWS) }
        colCount = { i: 0 for i in range(COLS) }
        locations = {} # num : (row, col) -- map each numberr in the `arr` to it's position in the matrix `mat`

        # Pre-populate the locations of each element in `arr` in the matrix
        for row in range(ROWS):
            for col in range(COLS):
                # Update the `locations` dict to map the tile's value to its (row, col) coordinates
                value = mat[row][col]
                locations[value] = (row, col)
        
        # Paint each cell sequentially until a full row or column is painted
        for i, num in enumerate(arr):
            # Fetch the `num`'s coordinates from the `locations` map
            row, col = locations[num]

            # Update the `rowCount` and `colCount`
            rowCount[row] += 1
            colCount[col] += 1

            # If the `row` or `col` has been completely filled, return the current index
            if rowCount[row] == COLS or colCount[col] == ROWS:
                return i
