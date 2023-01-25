class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0

        for n in nums:
            # If n - 1 does not exist in the set, we know n is the start of a sequence
            if n - 1 not in hashset:
                length = 1
                while n + 1 in hashset:
                    length += 1
                    n += 1
                longest = max(longest, length)

        return longest
