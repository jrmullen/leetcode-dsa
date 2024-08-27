class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = float('-inf') # Start at -infinity so the value is immediately overwritten
        
        # Bottom-up approach:
        # Iterate over `nums` calculating the product at each step
        # Track both the current maximum product and the current minimum product
        # Tracking the minimum is necessary for handling negative product, e.g. [4,-3,-2]
        currentMax = 1
        currentMin = 1

        for n in nums:
            maxProduct = n * currentMax
            minProduct = n * currentMin
            currentMax = max(maxProduct, minProduct, n)
            currentMin = min(maxProduct, minProduct, n)

            # Re-calculate the maximum product `result`
            result = max(result, currentMax, n)
        
        return result
