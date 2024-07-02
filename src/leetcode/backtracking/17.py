class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        combination = []

        # Map each number from the phone to its associated letters
        letters = {"2": "abc", "3": "def",  "4": "ghi",  "5": "jkl", "6": "mno", "7": "pqrs",  "8": "tuv",  "9": "wxyz"}

        def backtrack(i):
            # Base Case - all digits have been used
            if len(combination) == len(digits):
                if combination:
                    result.append(''.join(combination))
                return

            # Actions - iterate over each possible letter
            for c in letters[digits[i]]:
                combination.append(c)
                backtrack(i + 1)

                # Undo the above action
                combination.pop()

        backtrack(0) # Start at the first number
        return result
