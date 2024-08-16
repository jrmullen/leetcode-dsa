class Solution:
    def rob(self, nums: List[int]) -> int:
        n1 = 0
        n2 = 0

        for n in nums:
            sum = max(n1 + n, n2)
            n1 = n2
            n2 = sum

        return n2
