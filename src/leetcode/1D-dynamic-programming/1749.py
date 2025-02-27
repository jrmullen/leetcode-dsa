class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        result = 0
        prefix_max = 0
        prefix_min = 0
        current_total = 0

        # Iterate over each number in the `nums` list keeping a running total of the total sum `current_total`
        for num in nums:
            current_total += num

            # Update the `result` with the largest absolute sum encountered
            # The difference between the `current_total` and the `prefix_min` will be the subarray with the largest sum
            # The difference between the `current_total` and the `prefix_max` will be the subarray with the smallest sum
            result = max(result, abs(current_total - prefix_min), abs(current_total - prefix_max))

            # Re-calculate the `prefix_max` and `prefix_min` with the largest and smallest subarray sums
            prefix_max = max(prefix_max, current_total)
            prefix_min = min(prefix_min, current_total)

        return result
