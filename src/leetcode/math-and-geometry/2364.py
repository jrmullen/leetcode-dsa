class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        good = 0 # The number of good pairs
        count = defaultdict(int)

        # Intuition: the provided equation to validate `nums` can be arranged from `j - i = nums[j] - nums[i]`
        # into `nums[j] - j = nums[i] - i`. This means that for 2 elements `i` and `j` to be a good pair, they
        # must have the same difference between their value and their index.

        for i, num in enumerate(nums):
            # First calculate the difference between each value's position and value
            difference = num - i

            # Increment the count of good pairs by the current number of pairs sharing a `difference`
            good += count[difference]
            
            # Update the `diffs` count for the `difference`
            count[difference] += 1
        
        # Total number of pairs `(n * (n - 1)) // 2` minus the number of `good` pairs leave the bad pairs
        return (n * (n - 1)) // 2 - good
