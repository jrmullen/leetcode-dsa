class Solution:
    def integerBreak(self, n: int) -> int:
        # Bottom-up tabulation: rather than starting at `n` and working backwords, start at 1 and calculate the 
        # maximum product for each value to avoid repeated work

        # Base case: values 1, 2, 3 will have a maximum product of n - 1
        if n <= 3:
            return n - 1

        dp = [0] * (n + 1) # Store the maximum product for each number 0 to n
        dp[1] = 1 # Default: the maximum product of 1 is 1

        # Iterate over each number from 2 to n
        for num in range(2, n + 1):
            max_product = num # The maximum product will start as the `num`

            # Split the `num` into groups and compare their products
            for i in range(2, num):
                # The product of the group will be the `num` multiplied by the maximum product of `num - i`
                max_product = max(max_product, i * dp[num - i]) # Keep the largest value encountered
            
            dp[num] = max_product # Finally, store the `max_product` found across all possible groups in the `dp` list
        
        return dp[n] # The final value at index `n` will be the maximum product

        # Top-down memoization: recursively find the maximum product for each combination starting at `n` and
        # working backwards, caching the calculated values to avoid repeated work

        # Base case: values 1, 2, 3 will have a maximum product of n - 1
        # if n <= 3:
        #     return n - 1

        # @cache
        # def dp(num):
        #     if num <= 3:
        #         return num
            
        #     max_product = num
        #     for i in range(2, num):
        #         max_product = max(max_product, i * dp(num - i))
            
        #     return max_product
        
        # return dp(n)
