class Solution:
    def numSquares(self, n: int) -> int:
        squares = [1]

        # Generate a list of all perfect squares that are less than or equal to `n`
        i = 2
        while i <= sqrt(n):
            squares.append(i * i)
            i += 1
        
        # Build the solution
        result = 0

        # Tabulate the results
        dp = [i for i in range(n + 1)]

        # Iterate over each number from 0 to `n` and save the minimum number of perfect squares that sum into it
        for i in range(n + 1):
            # Consider each square that is less than `i`
            for square in squares:
                # Stop once a square larger than `i` is reached
                if square > i:
                    break
                
                # Subtract the `square` from `i` and then check if a value has already been calculated for the remaining
                # amount by checking the tabulated `dp` list
                difference = i - square
                dp[i] = min(dp[i], 1 + dp[difference]) # Update the `dp` list with the smallest value encountered
                
        # The last element in the `dp` list will contain the minimum value for `n`
        return dp[-1]
