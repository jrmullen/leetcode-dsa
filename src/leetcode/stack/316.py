class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = [] # Monotonic stack
        seen = set() # Track which characters have been used

        # Record the latest index that each character in the string occurs
        last_occurrence = { c: i for i, c in enumerate(s) }

        for i, c in enumerate(s):
            # Do not reuse characters
            if c not in seen:
                # Greedy: if the last letter is greater than c, remove it.
                # If the current character is not the last occurrence of the character, remove it.
                while stack and stack[-1] > c and i < last_occurrence[stack[-1]]:
                    seen.remove(stack.pop()) # Pop the top of the stack and mark it as unseen
                seen.add(c) # Mark the character as seen
                stack.append(c) # Add the character to the stack
        
        return ''.join(stack)
