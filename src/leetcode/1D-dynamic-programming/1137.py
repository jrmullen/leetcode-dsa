class Solution:
    def tribonacci(self, n: int) -> int:
        # Default cases for values <= 2
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        # Store the 3 most recent tribonacci numbers
        a = 0
        b = 1
        c = 1
        
        # Update the 3 most recent numbers for iterations 3 to n
        for _ in range(3, n + 1):
             a, b, c = b, c, a + b + c

        # Finally, return the most recently calculated number, `c`
        return c
