class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # Helper function to determine if a given weight can be shipped within the allowed days
        def canShipWeight(weight: int) -> bool:
            total = 0
            days_needed = 1
            for w in weights:
                total += w
                if total > weight:
                    total = w # Reset the total
                    days_needed += 1 # Increment the number of days needed
                    if days_needed > days: # Cannot exceed the number of allowed days
                        return False
            return True

        # Calculate the bounds of potential weights
        l = 0 # The minimum weight required will be the largest weight in the list of weights
        r = 0 # The maximum weight will be the total sum of all weights (e.g. ship everything in 1 day)
        for weight in weights:
            l = max(l, weight) # Track the largest number encountered for the left pointer
            r += weight # Sum the weights as the right pointer

        # Binary search to find the minimum weight
        while l <= r:
            mid = l + (r - l) // 2
            if canShipWeight(mid): # Use the helper function to determine if the weight can be shipped
                r = mid - 1 # Move the right pointer inward
            else:
                l = mid + 1 # Move the left pointer inward
        
        return l # The left pointer will end at the minimum weight
