class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        i_start = 0
        i_target = 0

        while i_start < n or i_target < n:
            # Skip all `_` in `start` until a character is found
            while i_start < n and start[i_start] == '_':
                i_start += 1
            
            # Skip all `_` in `target` until a character is found
            while i_target < n and target[i_target] == '_':
                i_target += 1
            
            # If only one of the strings reached the end, they cannot be the same
            if i_start == n or i_target == n:
                return (i_start == n and i_target == n)

            # Snapshot the current character of each string
            c_start = start[i_start]
            c_target = target[i_target]

            # If the characters are different the strings cannot be the same
            if c_start != c_target:
                return False
            
            # An `L` in the `target` string should always have a lower or equal index to the `start` string
            if c_start == 'L' and i_start < i_target:
                return False
            
            # An `R` in the `target` string should always have a greater or equal index to the `start` string
            if c_start == 'R' and i_start > i_target:
                return False
            
            i_start += 1
            i_target += 1
        
        return True
