class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        result = 0 
        
        # Sort the input
        nums.sort()

        # Binary search to find the smallest number in `nums` that is less than the `target`
        def binarySearch(l, r, target):
            while l <= r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return r

        # From every element in `nums` binary search to find the upper and lower bound
        for i in range(len(nums)):
            lowerBound = lower - nums[i] # The lower bound for valid values that can be combined with `nums[i]` to form a fair pair
            upperBound = upper - nums[i] # The lower bound for valid values that can be combined with `nums[i]` to form a fair pair
            
            # The number of possible pairs with `nums[i]` will be equal to the length of the window between the upper and lower bounds
            result += (
                binarySearch(i + 1, len(nums) - 1, upperBound + 1) - 
                binarySearch(i + 1, len(nums) - 1, lowerBound)
                )

        return result
