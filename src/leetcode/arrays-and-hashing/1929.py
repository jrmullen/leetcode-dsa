class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        N = len(nums)
        result = [0] * (2 * N) # Create an array of size 2n
        
        # Iterate over the list of nums
        for i, num in enumerate(nums):
            result[i] = num # Populate index i in the result list with the number
            result[i + N] = num # Populate index i + n
        
        return result
