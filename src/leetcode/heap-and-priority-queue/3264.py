class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # Push the list of `nums` into a Minheap
        heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)

        for _ in range(k):
            # Pop the smallest number off the heap and multiply it by the `multiplier`
            _, i = heapq.heappop(heap)

            # Multiply the number by the `multiplier` to get the new value
            nums[i] *= multiplier

            # Push the new number back onto the heap
            heapq.heappush(heap, (nums[i], i))
        
        return nums
