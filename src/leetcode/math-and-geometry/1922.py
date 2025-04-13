class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def fastExponentiation(x, power):
            # Base case: 0 raised to any power will be 0
            if x == 0:
                return 0

            # Base case: anything to the power of 0 is 1
            if power == 0:
                return 1

            result = fastExponentiation(x, power // 2) % MOD # Recursively calculate the value of half the exponent
            result = (result * result) % MOD # Multiply the `result` with itself to get the full exponential value

            # If `n` is odd, it needs to be multiplied by `x` one additional time to account for integer division rouning down
            # e.g. x^9 => x * (x^4 * x^4) => x * (x^2 * x^2) * (x^2 * x^2) => etc.
            return result if power % 2 == 0 else x * result % MOD

        # An even index may have even values 0,2,4,6,8 -- 5 types. A string of n digits will have floor((n + 1) / 2) even index
        # An odd index may have prime values 2,3,5,7 -- 4 types. A string of n digits will have floor(n / 2) odd indices
        # Therefore the number of good digits in a string of n digits will be 5^((n-1)/2) * 4^(n/2)
        # This exponent can be very large, so the solution can be optimized to logn time complixity using fast exponentiation
        return fastExponentiation(5, (n + 1) // 2) * fastExponentiation(4, n // 2) % MOD
