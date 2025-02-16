class Solution:
    def punishmentNumber(self, n: int) -> int:
        result = 0

        def canPartition(num, target):
            # Base case: invalid partition
            if target < 0 or num < target:
                return False
            
            # Base case: a partition summing to `target` has been found
            if num == target:
                return True
            
            # Recursively check all partitions of the current `num`
            return (
                canPartition(num // 10, target - num % 10) or
                canPartition(num // 100, target - num % 100) or
                canPartition(num // 1000, target - num % 1000)
            )

        # Iterate over each number from 1 to `n` (inclusive)
        for i in range(1, n + 1):
            square = i * i # Calculate the square

            # Recursively calculate the sum of each partition of the `square`. If it can be partitioned in a way
            # such that the sum is equal to `i`, the `square` is added to the `result`
            if canPartition(square, i):
                result += square

        return result
