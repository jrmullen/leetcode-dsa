 class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        count = 0

        for c in s:
            # If the character is different than the last character in the `result` list, reset the `count`
            if result and c != result[-1]:
                count = 0
            
            # If there are already 2 of the character, do not add any more
            if count == 2:
                continue
            
            # Increase the `count` and add the character to the `result` list
            count += 1
            result.append(c)
        
        return ''.join(result)
