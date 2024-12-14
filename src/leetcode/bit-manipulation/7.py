class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2**31 - 1 # 0xFFFFFFFF
        min_int = -2**31 # 0x7FFFFFFF

        result = 0
        while x:
                        # Snapshot the last digit of `x`
            digit = int(math.fmod(x, 10))

            # Chop the last digit off of `x`
            x = int(x / 10)
            
            # Multiply the result by 10 to shift the digits left 1 place, then finally add the new `digit`
            result = (result * 10) + digit

            # If at any point the `result` exceeds the min or max integer value, return `0`
            if result > max_int or result < min_int:
                return 0

        return result
