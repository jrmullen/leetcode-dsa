class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        visited = set()

        def backtrack(i, visited):
            # Base case - the end of the string has been reached
            if i == len(s):
                return 0
            
            # Track the maximum number of substrings in the loop 
            result = 0

            # Iterate over indexes from `i` to the end of the string `s`
            for j in range(i, len(s)):
                substring = s[i:j + 1]

                # If the substring has already been accounted for, skip it
                if substring in visited:
                    continue

                # Add the unique substring to the `visited` set
                visited.add(substring)

                # Backtrack, but keep track of the largest number of substrings encountered
                result = max(result, 1 + backtrack(j + 1, visited))

                # Undo the above decision by removing the `substring` from the `visited` set
                visited.remove(substring)

            # Return the maximum number of substrings found
            return result
        return backtrack(0, visited)
