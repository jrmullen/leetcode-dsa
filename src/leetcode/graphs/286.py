class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows = len(rooms)
        columns = len(rooms[0])
        INF = 2 ** 31 - 1
        q = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        distance = 1

        # Add each gate tile to the queue
        for r in range(rows):
            for c in range(columns):
                if rooms[r][c] == 0:
                    q.appendleft((r, c))

        # Multi-source BFS starting at each gate tile
        while q:
            # Process each "batch" before moving on to the next
            for _ in range(len(q)):
                row, col = q.pop()

                # Visit all neighboring tiles
                for dRow, dCol in directions:
                    newRow = row + dRow
                    newCol = col + dCol
                    # Only update empty room tiles that are within the bounds of the board
                    if (newRow in range(rows) and
                            newCol in range(columns) and
                            rooms[newRow][newCol] == INF
                    ):
                        rooms[newRow][newCol] = distance  # Update the empty tile
                        q.appendleft((newRow, newCol))

            # Increment the distance count
            distance += 1
