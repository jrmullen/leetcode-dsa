class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        number = 1 # Start at one

        # Iterate until `n` numbers have been added to the `result` list
        for _ in range(n)
            # Append each number to the `result` list as they are visited
            result.append(number)
            
            if number * 10 <= n:
                number *= 10 # Move down to the next level of the tree until the bottom is reached
            else:
                # If the target number `n`, or the end of a level (number ending in `9`) is reached, move up a level
                while number == n or number % 10 == 9:
                    number //= 10
                
                # Increment to visit the next number in the level
                number += 1

        return result
