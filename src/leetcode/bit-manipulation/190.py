class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        position = 31 # The position of the bit to be written to `result`. 32-bit int, so start at 31

        while n:
            # Take the least significant bit from `n` and add it to the `result` shifted by `position` to reverse it
            result += (n & 1) << position
            n >>= 1 # Shift `n` to the next bit
            position -= 1 # Decrement the `position` of the next bit to be written to the `result`
        
        return result
