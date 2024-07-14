class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python only has a minHeap, so convert `stones` to negative numbers so we can treat it as a maxHeap
        stones = [-s for s in stones]
        heapq.heapify(stones) # Convert the input list to a heap
        while len(stones) > 1:
            # `heapPop()` pops and returns the smallest value from the heap, 
            # but since `stones` has been converted to negative numbers it is actually the largest stone
            y = heapq.heappop(stones) # `y` is the largest stone
            x = heapq.heappop(stones) # `x` is the second largest stone

            # If the weights are different, `x` is smashed and `y` becomes `x - y`
            if x != y:
                heapq.heappush(stones, y - x)
        
        # The absolute value of the final element must be returned since `stones` was converted to negative numbers
        return abs(stones[0]) if stones else 0
