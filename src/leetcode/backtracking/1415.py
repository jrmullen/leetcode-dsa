class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []

        def backtrack(string):
            if len(string) == n:
                result.append(string)
                return
            
            # Create a combination using each letter
            for letter in ['a', 'b', 'c']:
                # Do not allow repeats
                if string and letter == string[len(string) - 1]:
                    continue
                
                
                string += letter # Add the latter to the string
                backtrack(string) # Recurse to create combinations using the new `string`
                string = string[:-1] # Undo the previous change (backtrack)
            return
        
        backtrack('')

        # If there are less than `k` strings, return an empty string
        return '' if k > len(result) else result[k - 1]
