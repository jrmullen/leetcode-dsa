class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # First, find the maximum number of candies
        maximum = max(candies)

        # Binary search to find the maximum number of candies
        l = 0
        r = maximum

        while l < r:
            # Round up the midpoint (+ 1) to avoid infinite loops
            mid = (l + r + 1) // 2

            # Determine how many children the piles can feed by splitting into piles of `mid`
            maxChildren = 0
            for pile in candies:
                maxChildren += pile // mid
    
            # If splitting the piles into size `mid` can feed `k` or more children, move the left pointer in
            if maxChildren >= k:
                l = mid
            else:
                # Otherwise move the right pointer in
                r = mid - 1
        
        return l
