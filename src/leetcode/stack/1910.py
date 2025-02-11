class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        n = len(part)

        for c in s:
            # Push the new character onto the stack
            stack.append(c)

            if len(stack) >= n and "".join(stack[-n:]) == part:
                # Pop all the characters of `part` off the stack
                for _ in range(n):
                    stack.pop()
            
        return "".join(stack)
