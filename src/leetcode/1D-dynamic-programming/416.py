class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Top-down approach: starting at the end of the `nums` list and working backwords,
        # compile a list of sums from each possible combination. If there exists a sum that
        # is equal to half of the sum of the `nums` list, it can be equally partitioned
        
        totalSum = sum(nums)

        # Equal partitions means that each partitioned list must equal half of the sum of `nums`
        # If half of the sum is an odd number, is it impossible to equally partition
        if totalSum % 2 == 1:
            return False
        
        # If there is a combination of numbers in `nums` that equal half the value, it can be equally paritioned
        target = totalSum // 2

        # Track the number of combinations in a `dp` set
        dp = set()
        dp.add(0)

        for n in nums:
            # Temporary set to work with while iterating over `dp`
            subset = set()
            for d in dp:
                # If the target is found, `nums` can be equally partitioned
                if n + d == target:
                    return True
                subset.add(n + d) # Add the sum to the temporary working set
            # Combine the sets to prepare for the next round of iterations
            dp = dp.union(subset)
        
        return False
