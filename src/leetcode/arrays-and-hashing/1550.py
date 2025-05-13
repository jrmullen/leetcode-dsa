class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0 # Count the number of even numbers in a row encountered
        for num in arr:
            if num % 2 == 0: # If the current number is even, reset the counter
                count = 0
                continue
            count += 1 # If the current number is odd, increment the counter
            if count == 3: # If the count ever hits 3, there are 3 odd numbers in a row
                return True
        return False
