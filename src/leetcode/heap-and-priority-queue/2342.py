class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sums = defaultdict(list) # digit sum : MAX heap of numbers summing to that

        # Iterate over each `num` in the list of `nums` and sum its digits as the `total`
        for num in nums:
            total = 0
            for digit in str(num):
                total += int(digit)
            
            # Map the `total` digit sum to the `num` by pushing it onto the heap
            heapq.heappush(sums[total], -num)
        
        result = -1 # Default case returns -1
        for heap in sums.values():
            # Each heap with more than one value will have its largest two numbers in the first and second positions
            if len(heap) < 2:
                continue
            
            # Add the two largest values from the top of the heap, tracking the largest sum encountered
            result = max(result, -heapq.heappop(heap) + -heapq.heappop(heap))
        
        return result
