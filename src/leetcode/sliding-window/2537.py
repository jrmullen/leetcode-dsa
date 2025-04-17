class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        result = 0
        l = 0
        count = defaultdict(int)
        pairs = 0

        # Sliding window over the list of nums
        for r in range(len(nums)):
            num = nums[r]
            pairs += count[num] # The new number can be paired will all previous instances of that number
            count[num] += 1 # Increase the count of the new number

            # Once a valid window is found, shrink the window to find the count of valid subarrays
            while pairs >= k:
                num = nums[l]
                result += len(nums) - r # All subarrays starting at the left pointer and ending at the right are valid
                pairs -= count[num] - 1 # Reduce the pair counter to acount for ejecting the left element
                count[num] -= 1 # Decrement the counter
                l += 1 # Move the left pointer forward

        return result
