class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Bottom up approach:
        # Start at the end of the array (the top of the staircase) and work backwards
        # Update the value of element `i + 1` (1 step above) with element `i + 2` (2 steps above)
        # and keep the lesser value
        for i in range(len(cost) - 3, -1, -1):
            p1 = cost[i] + cost[i + 1]
            p2 = cost[i] + cost[i + 2]
            cost[i] = min(p1, p2)
        
        # You can either start from index `0` or `1`, so return the smaller value
        return min(cost[0], cost[1])
