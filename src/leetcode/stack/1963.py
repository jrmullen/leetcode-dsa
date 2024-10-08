class Solution:
    def minSwaps(self, s: str) -> int:
        # Maintaining a physical stack is a waste of memory, so use an integer to count the "stack" size instead
        stack = 0

        # Iterate over the characters in `s`, eliminating `[]` pairs so all that is left on the "stack" are the mismatched characters
        for c in s:
            if c == '[':
                stack += 1 # Increase the count for `[`
            else:
                if stack == 0:
                    stack += 1 # If the stack is empty there is a mismatched pair, so increase the stack count
                else:
                    stack -= 1 # Decrease the count for `]`
        
        # Each swap can fix 2 imbalanced brackets. This results in a pattern
        # Swaps:        0 1 1 2 2 3 3 4 4
        # Mismatches:   0 1 2 3 4 5 6 7 8
        return (stack + 1) // 2
