class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        q = deque() # Queue contains tuple, (count, time it will be available to re-add to the heap)
        counts = Counter(tasks) # Creates a dictionary of letter:count
        maxHeap = [-c for c in counts.values()] # maxHeap in python - convert to negatiives
        heapq.heapify(maxHeap)

        while maxHeap or q:
            # Move time forward
            time += 1

            # Optimization - if no tasks to process on `maxHeap`, skip forward to next required time
            if not maxHeap and q:
                time = q[-1][1]
            else: # Pop the task with the highest count off the heap and add it to the queue
                task = heapq.heappop(maxHeap)
                if task < -1:
                    # Adding 1 to the task count since we're working with negative numbers
                    q.appendleft((task + 1, time + n))
        
            # Check to see if the head of the queue is eligible to be re-processed
            if q and q[-1][1] == time:
                qTask, _ = q.pop() # Remove the task from the queue
                heapq.heappush(maxHeap, qTask) # Push the task back onto the `maxHeap`

        return time
