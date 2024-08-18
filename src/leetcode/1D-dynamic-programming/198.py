class Solution:
    def rob(self, nums: List[int]) -> int:
        n1 = 0
        n2 = 0

        # Visit each house in `nums`, updating each element in place with the maximum value possible
        for n in nums:
            # Adjacent houses cannot be robbed, a comparison must be made between the adjacent house `n2`
            # and the new house `n`, which would be added to the running sum of loot from 2 houses ago, `n1`
            # Visualized - n1 n2 n
            sum = max(n1 + n, n2)

            # Move the pointers forward
            n1 = n2
            n2 = sum

        return n2
