class Solution:
    def clearDigits(self, s: str) -> str:
        stack = deque()

        for c in s:
            if c.isnumeric() and stack:
                stack.pop() # Pop the last character off the stack if the character is a numeric digit
            else:
                stack.append(c) # Push the character onto the stack if the character is a non-numeric digit
        
        # Finally, combine the characters on the stack into a string
        return "".join(stack)
