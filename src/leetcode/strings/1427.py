class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for direction, amount in shift:
            amount %= len(s) # Mod by the length of the string to eliminate unnecessary shifts
            if direction == 1:
                s = s[-amount:] + s[:-amount] # Right shift - move the end of the string to the front
            else:
                s = s[amount:] + s[:amount] # Left shift - move the start of the string to the end
        return s