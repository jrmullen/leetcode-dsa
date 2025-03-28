class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        ROWS, COLS = len(grid), len(grid[0])
        result = [0] * len(queries)
        score = 0 # Track the current score

        # Transform the list of `queries` into a list of tuples
        for i in range(len(queries)):
            queries[i]  = (queries[i], i) # (query, index)
        
        # Sort the queries in ascending order
        queries.sort()

        visited = set() # Track which tiles of the `grid` have already been visited previously
        heap = [] # minHeap

        # Push the starting point onto the heap
        heapq.heappush(heap, (grid[0][0], 0, 0)) # (value, row, col)

        # Mark the starting tile as visited
        visited.add((0, 0)) 

        # Intuition: since the queries are sorted in ascending order, the grid can be traversed via BFS in order without having to start over
        # with each query. The same running score can be used for each iteration. Values are pushed into a heap so that the smallest tiles
        # can be processed first to maximum score.
        for query, idx in queries:
            # Pop from the heap until it is either empty, or no values smaller than the `query` remain
            while heap and heap[0][0] < query:
                value, row, col = heapq.heappop(heap) # Pop the smallest value from the heap
                score += 1 # Score points

                # Attempt to visit all neighboring tiles
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_row = row + dr
                    new_col = col + dc

                    # If the new cell is within the bounds of the grid and has not previously been visited, addd it to the queue
                    if new_row >= 0 and new_col >= 0 and new_row < ROWS and new_col < COLS and (new_row, new_col) not in visited:
                        heapq.heappush(heap, (grid[new_row][new_col], new_row, new_col)) # Push the neighboring tile onto the heap
                        visited.add((new_row, new_col)) # Mark the new tile as visited

            result[idx] = score # Add the final `score` to the `result` list in the correct position

        return result
