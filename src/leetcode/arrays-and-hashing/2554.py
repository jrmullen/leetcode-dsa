class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        result = 0
        total = 0

        # Convert the list of banned characters into a set for efficient lookups
        banned = set(banned)

        for num in range(1, n + 1):
            # Skip banned numbers
            if num in banned:
                continue
            
            # If the `maxSum` is exceeded, return the `result` list
            if (total + num) > maxSum:
                return result
            
            total += num # Add the `num` to the `total` sum
            result += 1 # Increment the `result` counter to account for `num`

        return result
