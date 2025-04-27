class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        result = 0 # Track the number of valid subarrays encountered

        # Iterate over each element in the list of nums from 1 to n-1, acting as the midpoint of the triplet
        for middle in range(1, len(nums) - 1):
            if nums[middle] == (nums[middle - 1] + nums[middle + 1]): # Compare the `middle` element with both its neighboring numbers
                result += 1 # If the `middle` element is equal to half the sum of its neighbors, increase the `result` counter
        
        return result
