class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        ROWS = len(moveTime)
        COLS = len(moveTime[0])
        heap = [(0, 0, 0)] # minHeap of tuples (time, x, y). Start at (0, 0) with time 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        min_time = [[float('INF') for _ in range(COLS)] for _ in range(ROWS)] # Track the minimum time to get to each visited cell
        min_time[0][0] = 0 # The starting point (0, 0) takes 0 time

        while heap:
            time, row, col = heapq.heappop(heap) # Pop the fastest move off the heap

            # Base case: the target cell has been reached
            if row == ROWS - 1 and col == COLS - 1:
                return time
            
            if min_time[row][col] == time:
                for dx, dy in directions:
                    new_row = row + dx
                    new_col = col + dy

                    # Do not leave the bounds of the board
                    if new_row < 0 or new_col < 0 or new_row == ROWS or new_col == COLS:
                        continue

                    # If the `moveTime` is larger than the current `time`, we must wait. Therefore always use the larger value of the two
                    total_time = max(time, moveTime[new_row][new_col]) + 1 # Add 1 second to account for moving

                    # If `total_time` is smaller than the current `min_time`
                    if total_time < min_time[new_row][new_col]:
                        min_time[new_row][new_col] = total_time # Update to reflect the new minimum
                        heapq.heappush(heap, (total_time, new_row, new_col)) # Push the cell onto the minHeap
