class Solution:
    def hammingWeight(self, n: int) -> int:
        # Cheater solution using built-in functions:
        # return n.bit_count()

        result = 0
        while n:
            result += n & 1 # Compare the least significant bit. If it is a 1, increase the `result` counter
            n >>= 1 # Shift to the next bit
        return result
