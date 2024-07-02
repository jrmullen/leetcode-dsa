class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        result = r # Default to the max value, because we know that is the worst-case solution

        # Binary search to speed up finding the optimal k value
        while l <= r:
            k = (l + r) // 2

            time = 0 # Track the total amount of time it takes to eat all of the bananas
            for p in piles:
                time += math.ceil(p / k) # # of bananas p / k eaten per hour = total time to eat a pile
            
            if time > h: # If it took longer than h hours, we need a larger k
                l = k + 1
            elif time <= h: # If it took less than h hours we have a potential result
                result = min(result, k) # Update the result to track the smallest k encountered
                r = k - 1
        return result # Return the smallest k found
