class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = [0 for _ in range(2 * n)] # Prepopulate the result array
        
        for i in range(n):
            result[2 * i] = nums[i] # Add index i to the result
            result[2 * i + 1] = nums[n + i] # Add index n + i to the result
        
        return result
