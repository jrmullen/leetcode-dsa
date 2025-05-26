class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            # If `c` is not a closing bracket, push it onto the stack
            if c != ']':
                stack.append(c)
                continue
            
            # Otherwise c is a closing bracket; build a string from what's on the stack
            substring = ''

            # Pop from the stack until an opening bracket is encountered
            while stack[-1] != '[':
                substring = stack.pop() + substring # Prepend the character from the stack to the current `substring`
            
            stack.pop() # Pop the opening bracket '[' off the stack

            # The opening bracket was found, so now we must determine the `k` value before the opening bracket
            k = '' # `k` may be multiple digits, so continue popping from the stack until the value is no longer numeric
            while stack and stack[-1].isdigit():
                k = stack.pop() + k # Prepend the value from the top of the stack
            
            # Append the final `substring` back onto the stack
            stack.append(int(k) * substring)

        # Finally, build and return the final result string by concatenating all of the substrings on the `stack` together
        return "".join(stack)
