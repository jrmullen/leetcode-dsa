class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        result = 0
        minHeap = [] # (num, i)
        maxHeap = [] # (-num, i)
        
        l = r = 0
        while r < len(nums):
            # Push the new value onto the heaps
            heapq.heappush(minHeap, (nums[r], r))
            heapq.heappush(maxHeap, (-nums[r], r))

            # If the window is no longer valid, shrink it until it is once again valid or the left pointer reaches
            # the right pointer
            while l < r and -maxHeap[0][0] - minHeap[0][0] > 2:
                l += 1

                # Remove values from the heaps containing values outside of the window
                while minHeap and minHeap[0][1] < l:
                    heapq.heappop(minHeap)
                while maxHeap and maxHeap[0][1] < l:
                    heapq.heappop(maxHeap)
            
            # Update the result count and move the right pointer forward
            result += (r - l) + 1
            r += 1

        return result
