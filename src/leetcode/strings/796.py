class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # If the strings are of different length they will never match
        if len(s) != len(goal):
            return False
        
        # Concatenate `s` onto itself to get the fully shifted string
        s = s + s

        # Compare the strings
        return goal in s
