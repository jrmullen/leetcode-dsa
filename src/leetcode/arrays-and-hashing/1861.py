class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])

        # Update the existing `box` matrix in-place
        for row in range(m):
            # Track the last cell that would be "blocking" so only 1 pass of each `row` is required
            # Start each row out of bounds at position `n`
            lastBlocker = (row, n)
            for col in range(n - 1, -1, -1): # Start at the rightmost element and work backwards to the left
                cell = box[row][col]
                if cell == "*":
                    # If the cell contains an obstacle set it as the `lastBlocker`
                    lastBlocker = (row, col)
                elif cell == "#":
                    # If the cell contains a rock and the cell immediately to the right is not a blocker, update in place
                    if lastBlocker != (row, col + 1):
                        x, y = lastBlocker
                        box[x][y - 1] = "#"
                        box[row][col] = "."
                        lastBlocker = (x, y - 1) # Set the rock `lastBlocker`
                    else:
                        # If the cell immediately to the right is a blocker, the rock doesn't move, but it becomes the `lastBlocker`
                        lastBlocker = (row, col)

        # Generate an empty vertical `box`
        result = [["" for _ in range(m)] for _ in range(n)]
        for row in range(n):
            for col in range(m):
                result[row][col] = box[col][row] # Populate the transposed `box`

        # Finally, reverse each row to finish the 90 degree rotation
        for row in range(n):
            result[row].reverse()

        return result
