class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        result = 0

        # Sort the list of `nums` - this is possible since the goal is to find a subsequence of identical numbers.
        # Therefore the order does not matter
        nums.sort()

        # Sliding window to find the longest window where all numbers meet the criteria.
        # Rather than applying the "operation" each time, we only need to check that the numbers in the range all are within
        # the allowed range if the operation were to be applied
        l = 0
        for r in range(len(nums)):
            # If the new `r` value invalidates the window, shrink it by moving the `l` pointer forward until it is once again valid
            while nums[r] - nums[l] > (2 * k):
                l += 1

            # Update the `result` with the largest window encountered
            result = max(result, (r - l) + 1)

        return result
