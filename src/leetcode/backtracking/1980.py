class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result = []
        strings = set(nums) # Convert the list of `nums` to a set for faster lookups

        def backtrack():
            # Base case: a string of length n has been found
            if len(result) == len(nums):
                string = "".join(str(n) for n in result)
                return string not in strings # If the string is unique return True
            
            # Try each possible binary number
            for num in [0, 1]:
                result.append(num)

                # If the final binary string was found, stop iterating
                if backtrack():
                    return True
                
                # Undo the previous decision (backtrack)
                result.pop()
            
            return False

        # Backtrack until a unique binary string is found
        backtrack()
        return "".join(str(n) for n in result)
