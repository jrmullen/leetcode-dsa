class Solution:
    def checkValidString(self, s: str) -> bool:
        openMin = 0 # Track the minimum `(` with all wildcards being closing parens
        openMax = 0 # Track the maximum `(` with all wildcards being opening parens

        for c in s:
            if c == '(': # Open paren - increment both the min and max
                openMin += 1
                openMax += 1
            elif c == ')': # Closed paren - decrement both the min and max
                openMin -= 1
                openMax -= 1
            else: # Wildcard - account for both possible parenthesis
                openMin -= 1 # Decrement the minimum to account for a potential `)`
                openMax += 1 # Increment the maximum to account for a potential `(`

            # If the minimum ever drops below 0, reset it back  to 0            
            if openMin < 0:
                openMin = 0

            # If the maximum ever drops below zero it is impossible to balance the parenthesis
            if openMax < 0:
                return False
        
        # Finally, if there are 0 remaining open parenthesis the string is valid
        return openMin == 0
