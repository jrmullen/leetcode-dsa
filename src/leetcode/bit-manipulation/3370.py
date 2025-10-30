class Solution:
    def smallestNumber(self, n: int) -> int:
        result = 0
        msb = 0 # Most significant bit position

        # Count the number of bits in n by right shifting until there are no more set bits
        while n != 0:
            n >>= 1
            msb += 1 
        
        # Generate the final result with all bits set by shifting a 1
        for _ in range(msb):
            result <<= 1
            result |= 1
        
        return result
