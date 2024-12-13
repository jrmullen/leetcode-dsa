class Solution:
    def findScore(self, nums: List[int]) -> int:
        result = 0

        # Push the lists of `nums` into a heap
        heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)

        # Track elements that have been marked
        marked = set()

        while heap:
            # Pop the smallest number off the `heap`
            num, i = heapq.heappop(heap)

            # If the index of the popped tuple has previously been marked, skip processing it
            if i in marked:
                continue

            # Add the smallest number to the total `result` score
            result += num

            # Mark the smallest number's index along with its neighbors
            marked.add(i)
            marked.add(i - 1)
            marked.add(i + 1)
        
        return result
