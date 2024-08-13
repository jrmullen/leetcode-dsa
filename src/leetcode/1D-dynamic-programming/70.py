class Solution:
    def climbStairs(self, n: int) -> int:
        # If there is only 1 step in the staircase there is only 1 choice to be made
        if n == 1:
            return n
        
        # Bottom up approach:
        # The final step (the top of the staircase) is the base case - default value of 1
        # The second to last step (1 step down from the top) will always have only 1 step to go
        
        # Maintain 2 pointers to progress through the steps
        n1, n2 = 1, 1

        for i in range(n - 1):
            # Each time a new step is visited it will require the sum of the 2 previous steps beforer it
            sum = n1 + n2 # Calculate the sum of the previous 2 steps (e.g. step 3 = step 1 + step 2)
            n1 = n2 # `n1` is updated to contain the old `n2` value
            n2 = sum # `n2` is updated to contain the new value, `sum`
        
        # Finally, return the final sum of `n2`
        return n2
