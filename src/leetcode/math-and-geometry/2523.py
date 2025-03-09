class Solution:
    def closestPrimes(self, left, right):
        result = [-1, -1]
        min_difference = float("inf")

        # First, use the Sieve of Eratosthenes algorithm to generate a list of all primes up to the `right` integer
        isPrime = [True for _ in range(right + 1)]

        # 0 and 1 are not prime numbers, so overwrite their values
        isPrime[0] = False
        isPrime[1] = False

        # Flag all non-prime numbers
        for num in range(2, int(right ** 0.5) + 1):
            if isPrime[num]:
                # Mark all multiples of `num` as not prime
                for multiple in range(num * num, right + 1, num):
                    isPrime[multiple] = False

        # Collect all prime numbers that fall between `left` and `right`, inclusive
        primes = [num for num in range(left, right + 1) if isPrime[num]]

        # Finally, find the prime pair with the smallest difference
        if len(primes) < 2:
            return result  # Less than two primes

        for i in range(1, len(primes)):
            difference = primes[i] - primes[i - 1]
            if difference < min_difference:
                min_difference = difference
                result = [primes[i - 1], primes[i]]

        return result
