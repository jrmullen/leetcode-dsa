class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF # 32 1-bits
        max_int = 0x7FFFFFFF # The maximum 32-bit integer, equivalent to decimal `2147483647`

        # Intuition: Adding two numbers together can be done by XORing them, e.g. 1 + 2 = 3 (01 ^ 10 = 11)
        # However, this does not account for 1's that would require a carried bit
        # e.g. 1 + 1 = 2 (01 ^ 01 = 00)
        # To account for the carried bit the two numbers can be ANDed together and then shifted to the left by 1 bit

        # Continue interating until there is no longer a `carry` value
        while b != 0:
            carry = (a & b) << 1 # AND to get the carry
            a = (a ^ b) & mask # XOR to get the added value, ANDing with the `bitmask` to keep only 32 relevant bits
            b = carry & mask # AND the `carry` with the `bitmask` to keep only 32 relevant bits
        
        # If `a` is not less than the maximum integer value, XOR with the `bitmask` to get the 32 relevant bits,
        # but the XOR inverts the current bits, so that must be undone with a NOT `~`
        return a if a < max_int else ~(a ^ mask)
