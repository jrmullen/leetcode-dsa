class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = [-1 for _ in range(len(nums))]
        sorted_nums = sorted(nums) # Sort in ascending order
        indexes = {} # num: index of first occurrence

        # Store the index of the first occurrence of each number in the sorted list
        for i, num in enumerate(sorted_nums):
            if num not in indexes:
                indexes[num] = i

        # Populate the result array using the indexes
        for i, num in enumerate(nums):
            result[i] = indexes[num]
        
        return result
