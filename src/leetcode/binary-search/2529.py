class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Track where the negative values stop and where the positive values begin. Values of 0 can be ignored
        negative_end = len(nums) # Default to the end of the list
        positive_start = len(nums)

        # First, binary search to find the first index that's above or equal to 0
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < 0: # If the midpoint is less than 0, move the left pointer in
                l = mid + 1
            else: # Otherwise snapshot the midpoint as potentially the first non-negative number and move the right pointer in
                r = mid - 1
                negative_end = mid
            
        # Next, binary search to find the first index that's greater than 0
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] <= 0: # If the midpoint has a value of 0, move the left pointer in
                l = mid + 1
            else: # Otherwise the value must be > 0
                r = mid - 1
                positive_start = mid
        
        # The positive values will be everything from the `positive_start` index to the end of the list
        positives = len(nums) - positive_start
        # The negative values will be everything from index 0 to the `negative_end` index
        negatives = negative_end

        # Finally, return the larger value between the two
        return max(positives, negatives)
