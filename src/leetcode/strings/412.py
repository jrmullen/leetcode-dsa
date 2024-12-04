class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        # Iterate from 1 -> `n`
        for i in range(1, n + 1):
            word = ''
            
            if not i % 3: # If `i` is divisible by 3
                word += 'Fizz'
            if not i % 5: # If `i` is divisible by 5
                word += 'Buzz'
            
            # If the number was not divisible by 3 or 5 the string will still be empty
            if not word:
                word += str(i)
            
            # Finally, append the `word` to the `result` list
            result.append(word)

        return result
