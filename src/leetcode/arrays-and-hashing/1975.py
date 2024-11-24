class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        smallest = float('inf')
        negatives = 0

        # Intuition: count the number of negative numbers in the `matrix`. If there is an odd number every number can be 
        # flipped except for 1. Take the smallest number encountered, make it negative and subtract it from the total sum
        for row in matrix:
            for num in row:
                # Count the number if negative numbers encountered
                if num < 0:
                    negatives += 1
                
                # Add the absolute value of each number to the `total` sum
                total += abs(num)

                # Track the smallest number encountered.
                # IMPORTANT: do not only include negatives or 0 will be missed
                smallest = min(smallest, abs(num))
        
        # If there are an odd number of negative numbers subtract the `smallest` value in the `matrix` from the `total` sum
        if negatives > 0 and negatives % 2 == 1:
            total -= (2 * smallest) # Multiply the `smallest` number by 2 since it was previously included in the `total` sum
        
        return total
