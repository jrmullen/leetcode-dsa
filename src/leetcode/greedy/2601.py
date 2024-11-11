class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # Calculate prime numbers
        def isPrime(number):
            for f in range(2, int(sqrt(number)) + 1):
                if number % f == 0:
                    return False
            return True

        # Pre-populate `primes` with the largest prime number that is less than `primes[i]`
        prevPrime = 0
        primes = [0, 0] # Pre-populate 0 and 1
        for i in range(2, max(nums) + 1):
            if isPrime(i): # If `i` is prime, use its value and update `prevPrime`
                primes.append(i)
                prevPrime = i
            else: # If `i` is not prime, use the `prevPrime` number
                primes.append(prevPrime)

        prevNum = 0
        for num in nums:
            upperBound = num - prevNum - 1 # Subtract the previous value from the current `num`, non-inclusive
            num -= primes[upperBound] # Now subtract the largest prime number that is less than the upper bound
            
            if num <= prevNum:
                return False

            # Finally, update `prevNum` to use the new value
            prevNum = num
        
        return True
