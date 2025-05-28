class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # First, convert the binary strings to their integer values
        a, b = int(a, 2), int(b, 2)

        # To perform addition without actually using addition (+), the operation can be split into 2 parts
        # 1) Addition. To "add" 2 bits together, perform a bitwise XOR. However, this does not include the carry.
        # 2) Carry value. When a 1 is added to a 1, the result is a 0, but the 1 is carried to the next significant bit,
        # so left shift by 1 bit
        while b:
            bin_sum = a ^ b # Addition without considering the carry value is just a bitwise XOR
            carry = (a & b) << 1 # For the carry we want the bitwise & value, shifted 1 bit to the left so it's applied to the next bit

            # Update for the next iteration
            # set `a` and the binary sum, and `b` as the carry value
            a, b = bin_sum, carry
              
        # Finally, return the final sum `a` as binary
        return bin(a)[2:] # Trim the "0b" python junk
