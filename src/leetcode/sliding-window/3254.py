class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        result = []
        l = 0
        count = 1 # Count of consecutive numbers in the window

        for r in range(len(nums)):
            # If the right pointer is equal to the next value, increase the consecutive `count`
            if r > 0 and nums[r] == nums[r - 1] + 1:
                count += 1
            
            # If the window exceeds size `k`, the left pointer `l` must be shifted
            if r - l + 1 > k:
                # If `l` was a consecutive value, decrease the consecutive `count`
                if nums[l] + 1 == nums[l + 1]:
                    count -= 1
                l += 1 # Shift the pointer

            # If the window is of size K append a value to the `result` list
            if r - l + 1 == k:
                result.append(nums[r] if count == k else -1)
            
        return result
