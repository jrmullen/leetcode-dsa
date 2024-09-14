class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Approach:
        # The bitwise AND operation with a larger number and a smaller number will always result 
        # in a number less than or equal to the smaller number.
        
        result = 0
        largestNum = max(nums) # Identify the largest number in `nums`
        streak = 0 # Count the number of times `largestNum` appears consecutively

        for n in nums:
            if n == largestNum:
                streak += 1 # Increase the `streak` for consecutive elements
            else:
                streak = 0 # If a different number appears, reset the `streak`
            
            # Track the largest consecutive `streak`
            result = max(streak, result)
        
        return result
