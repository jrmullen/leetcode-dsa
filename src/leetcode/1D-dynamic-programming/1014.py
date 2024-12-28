class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        result = 0 
        max_val = values[0] - 1 # Start with the first value, subtracting 1 to account for starting at the second element in the loop

        for i in range(1, len(values)):
            # Calculate and keep the largest possible score.
            # The score will be the `max_val` encountered plus the current value, `values[i]`
            result = max(result, max_val + values[i])
            
            # Re-cacalculate the `max_val` to account for the newly encountered value.
            # Subtract 1 from each value to account for the distance increasing when calculating the next iteration
            max_val = max(values[i] - 1, max_val - 1)
        
        return result
