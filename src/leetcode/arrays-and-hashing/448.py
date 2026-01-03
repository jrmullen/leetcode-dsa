class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        N = len(nums) + 1 # Snapshot the size of the nums list before converting to a set
        nums = set(nums) # Convert to a set for optimized lookups

        # Find the numbers between 1 and N that are missing
        for i in range(1, N):
            if i not in nums:
                result.append(i)
        
        return result
 