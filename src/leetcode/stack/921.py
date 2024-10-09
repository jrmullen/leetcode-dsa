class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for c in s:
            # Cancel out matching parenthesis by popping from the stack
            if stack and stack[-1] == '(' and c == ')':
                stack.pop()
            else:
                stack.append(c) # Add opening and unmatched closing parenthesis to the stack
        
        # Each remaining parenthesis is unmatched and will need a pair to be valid
        return len(stack)
