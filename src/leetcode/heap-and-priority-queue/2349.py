class NumberContainers:

    def __init__(self):
        self.values = {} # Index : value
        self.indexes = defaultdict(list) # Value : minHeap of indexes

    def change(self, index: int, number: int) -> None:
        # Map value -> index and index -> value
        self.values[index] = number
        heapq.heappush(self.indexes[number], index)

    def find(self, number: int) -> int:
        if number not in self.indexes:
            return -1
        
        # Check the top of the heap to see if the index maps to the expected number
        heap = self.indexes[number] 
        while heap:
            index = heap[0]
            if number == self.values[index]:
                return index
            
            # If the number's don't match the index is stale and can be popped off the heap
            heapq.heappop(heap)

        return -1
        

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
