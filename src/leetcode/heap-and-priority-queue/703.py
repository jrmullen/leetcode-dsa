class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap) # Convert the input list into a heap

        # Pop elements from `minHeap` until there are exactly `k` elements
        # Since `heappop()` ejects the smallest value from the heap, and exactly `k` elements are maintained, 
        # the 0th element will always be the Kth largest element
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Push `val` onto the minHeap
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            # Eject the smallest value from the heap to maintain `k` elements
            heapq.heappop(self.minHeap)
        # Return the smallest value
        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
