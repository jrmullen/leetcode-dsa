class Solution:
    def minimumSize(self, nums, max_operations):
        
        def isDivisible(maxBalls):
            operations = 0
            for num in nums:
                # Calculate the number of operations it would take to divide `num` into numbers less than `maxBalls`
                operations += ceil(num / maxBalls) - 1
                if operations > max_operations:
                    return False
            return True
        
        # Binary search to find the smallest number from 1 to the largest number in `nums` that is divisible by `maxBalls`
        l, r = 1, max(nums)
        while l < r:
            m = (l + r) // 2
            if isDivisible(m):
                r = m
            else:
                l = m + 1
        return l
