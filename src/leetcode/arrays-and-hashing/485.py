class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        count = 0

        for num in nums:
            if not num:
                result = max(result, count) # Compare the count with the current largest
                count = 0 # Reset the count
            else:
                count += 1 # Count the 1

        return max(result, count)
