class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        result = -1
        count = defaultdict(int)

        # Count the number of times each number in `nums`
        for num in nums:
            count[num] += 1
        
        # Iterate over the `count` dict and update the `result` with the largest number with a count of `1`
        for num in count:
            if count[num] == 1:
                result = max(result, num)
        
        return result
