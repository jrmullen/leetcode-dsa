class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # Approach: leverage XOR  bitise operation to determine the number of differing bits
        # The result is 1 if the bits are different, and 0 if they are the same
        # e.g. 0011 XOR 0101 would result in 0110
        result = 0
        xor = start ^ goal # `^` will perform a logical XOR bitwise operation
        while xor:
            # Compare the least significant bit. A `1` means the bits are different, so increment the count
            result += xor & 1
            xor >>= 1 # Shift to the next bit
        
        return result
