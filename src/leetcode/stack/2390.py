class Solution:
    def removeStars(self, s: str) -> str:
        stack = [] # Stack to track visited charaters

        # Iterate over each character in the string `s` from left to right
        for char in s:
            if char != '*': # It is not the `*` character - push it onto the `stack`
                stack.append(char)
            else: # It is the `*` character - perform the "operation" by popping the previous char off the stack
                stack.pop()
        
        # Finally, join the remaining characters back into a string and return its value
        return ''.join(stack)
