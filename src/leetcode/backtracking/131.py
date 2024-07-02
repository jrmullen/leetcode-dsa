class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        partitions = []

        def backtrack(i):
            # Base case
            # If all partitions have been visited then they were all palindromes
            if i >= len(s):
                result.append(partitions.copy())
                return

            # Actions
            # Loop over all possible partitions
            for j in range(i, len(s)):
                # If the partition is a palindrome, add it to the partitions array and continue backtracking the DFS
                part = s[i:j + 1]
                if part == part[::-1]:
                    partitions.append(part)
                    backtrack(j + 1)
                    # Undo the above action
                    partitions.pop()

        # Start at index 0
        backtrack(0)
        return result
