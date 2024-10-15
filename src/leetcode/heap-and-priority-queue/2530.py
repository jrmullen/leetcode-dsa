class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        result = 0
        nums = [-n for n in nums] # Convert `nums` to negative numbers (Python hack to build a max heap)
        heapq.heapify(nums) # Heapify `nums` into a max heap

        while k > 0:
            largest = -heapq.heappop(nums) # Pop the largest number off the heap
            result += largest # Increase the score
            heapq.heappush(nums, -math.ceil(largest / 3)) # Modify `largest` and push the new value back onto the heap
            k -= 1 # Decrement the `k` counter

        return result
