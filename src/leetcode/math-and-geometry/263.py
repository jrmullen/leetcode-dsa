class Solution:
    def isUgly(self, n: int) -> bool:
        # Base base: ugly numbers must be positive integers
        if n < 1:
            return False
        
        # Consider each prime factor, starting with the largest to reduce the number of iterations
        for factor in (5, 3, 2):
            # while `n` is wholly divisable by the prime factor, continue dividing it
            while n % factor == 0:
                n //= factor
        
        return n == 1
