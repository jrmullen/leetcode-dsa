class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r = len(s1) - 1 # The window will always be the length of s1
        count_s1 = {}
        count_s2 = {}

        if len(s2) < len(s1):
            return False

        # Populate the character count of s1
        for c in s1:
            count_s1[c] = 1 + count_s1.get(c, 0)
        
        # Populate the character count of s2
        for c in s2[0:len(s1)]:
            count_s2[c] = 1 + count_s2.get(c, 0)

        for l in range(len(s2)):
            if count_s1 == count_s2:
                return True
            
            # Decrement the count of L. If it is 0, remove it from the dict
            count_s2[s2[l]] -= 1
            if count_s2[s2[l]] == 0:
                del count_s2[s2[l]]
            
            # Shift the window
            l += 1
            r += 1

            # If R passes the end of the string, loop back to the beginning
            if r == len(s2):
                r = 0
            count_s2[s2[r]] = 1 + count_s2.get(s2[r], 0)
        return False
      
