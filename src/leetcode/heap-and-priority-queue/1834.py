class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        result = []
        tasks = [(enqueue_time, i, processing_time) for i, [enqueue_time, processing_time] in enumerate(tasks)] # Add original index
        tasks.sort() # Sort by ascending `enqueue_time`
        task_idx = 0 # Pointer to the next task
        t = tasks[0][0] # Track the current time . Start at the `enqueue_time` of the first process
        heap = [] # minHeap (processing_time, index)

        while task_idx < len(tasks) or heap:
            # First, add all available processes from the list of tasks to the heap
            while task_idx < len(tasks) and tasks[task_idx][0] <= t:
                _, index, processing_time = tasks[task_idx]
                heapq.heappush(heap, (processing_time, index)) # Push the process onto the heap
                task_idx += 1 # Move the task index pointer forward

            # If there is no available process the CPU will idle until the next process is scheduled, and time can jump forward
            if not heap:
                t = tasks[task_idx][0] # Update time `t` to be the time the next available process is scheduled
                continue

            # Finally, pick up the process with the shortest `processing_time` and process it
            (processing_time, index) = heapq.heappop(heap) # Pop the next process off of the heap
            result.append(index) # Push the process's original index into the `result` list
            t += processing_time # Update time `t`

        return result
