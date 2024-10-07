class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for c in s:
            # If the stack is empty, add the character
            if not stack:
                stack.append(c)
                continue
            # If the character on the top of the stack prepended to the current character `c` is `AB` or `CD`
            # pop the top character off of the stack
            if stack[-1] + c == 'AB' or stack[-1] + c == 'CD':
                stack.pop()
            else:
                # Otherwise it's a legal character combination, so add the character to the stack
                stack.append(c) 
        
        return len(stack)
