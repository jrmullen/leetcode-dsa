class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {')': '(', ']': '[', '}': '{', }
        for char in s:
            # If the map does not contain our character, we know it is an opening character
            if map.get(char) is None:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if map.get(char) != stack[len(stack) - 1]:
                    return False
                else:
                    stack.pop()

        return len(stack) == 0
