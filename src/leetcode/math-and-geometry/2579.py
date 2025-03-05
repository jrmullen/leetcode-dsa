class Solution:
    def coloredCells(self, n: int) -> int:
        result = 1 # Starting point is 1 single cell

        # Iterate over each unit of "time" from 1 to `n`
        for i in range(1, n):
            # Looking at the pattern from the first few sequences there will be 1, 4, 8, 12 tiles.
            # The number of tiles will increase by `4 * i`
            result += 4 * i
        
        return result
