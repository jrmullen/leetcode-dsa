class Solution:
    def myPow(self, x: float, n: int) -> float:
        def func(x, n):
            # Base case: if `x` is 0, the result will always be 0
            if x == 0:
                return 0
            
            # Base case: anything raised to the power of 0 will be 1
            if n == 0:
                return 1

            result = func(x, n // 2) # Recursively calculate the value of half the exponent
            result = result * result # Multiply the `result` with itself to get the full exponential value

            # If `n` is odd, it needs to be multipliedd by `x` one additional time to account for integer division rouning down
            # e.g. x^9 => x * (x^4 * x^4) => x * (x^2 * x^2) * (x^2 * x^2) => etc.
            return result if n % 2 == 0 else result * x
        
        # Calculate the exponential result ignoring the sign of `n`
        result = func(x, abs(n))

        # If `n` is negative, account for that now by making it the denominator
        return result if n >= 0 else 1 / result
