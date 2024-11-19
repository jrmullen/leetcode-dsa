class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        l = 0
        total = 0 # Track the total sum of all numbers within the window
        store = set() # HashSet to store numbers for efficient lookups

        for r in range(len(nums)):
            # If the size of the window is > k, or the right pointer's number `nums[r]` is already in the `store`
            # remove the leftmost value from the `store` and `total` and shift the pointer forward to shrink the window
            while (r - l + 1) > k or nums[r] in store:
                store.remove(nums[l])
                total -= nums[l]
                l += 1
            
            # Add the right pointer's new number to the `store` and `total` sum
            store.add(nums[r])
            total += nums[r]

            # If the window is of size `k` update the `result` with the largest `total` encountered
            if (r - l + 1) == k:
                result = max(result, total)
        
        return result
