class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        result = 0

        # If there are less than 2 numbers exit immediately
        if len(nums) < 2:
            return result
        
        # Push `nums` into a minHeap
        heapq.heapify(nums)
        
        # Perform the operation until the smallest number is greater than or equal to `k`
        while nums[0] < k:
            result += 1 # Increment the `result` counter to account for the "operation"
            x = heapq.heappop(nums) # Pop the 2 smallest elements from the list of `nums`
            y = heapq.heappop(nums)

            # Generate the new number and push it onto the `heap`
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))

        return result
