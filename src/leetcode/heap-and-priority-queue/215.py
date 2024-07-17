class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Take the first K values of `nums` and heapify them
        minHeap = nums[:k]
        heapq.heapify(minHeap)

        # Iterate over the rest of `nums`
        for num in nums[k:]:
            # If the `num` is larger than the smallest value on the heap, pop the smallest value off and push `num`
            if num > minHeap[0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, num)
        
        # Since `minHeap` is maintained at size `k`, `minHeap[0]` will contain the Kth largest element
        return minHeap[0]
