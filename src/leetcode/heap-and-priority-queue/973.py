class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        result = []
        
        # Calculate the distance for each point
        for point in points:
            x, y = point
            distance = (x ** 2) + (y ** 2) # Note: taking the square root is unnecessary
            minHeap.append((distance, point)) # `distance` is the first element so we can sort by distance
        
        # Heapify to convert the list to a minHeap
        heapq.heapify(minHeap) # `heapify()` will key on the first element of `minHeap`

        # Populate `result` with the `k` shortest distances
        for i in range(k):
            _, point = heapq.heappop(minHeap) # `heapq.heappop()` pops and returns the smallest value from the heap
            result.append(point)
        
        return result
