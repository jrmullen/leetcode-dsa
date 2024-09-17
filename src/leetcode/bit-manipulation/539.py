class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Convert the `timePoints` into integers representing number of minutes
        for i, tp in enumerate(timePoints):
            h, m = tp.split(':') # Split by `:` to get hour and minute values
            timePoints[i] = (int(h) * 60) + int(m)
        
        # Sort in ascending order
        timePoints.sort()

        previous = len(timePoints) - 1

        # Pre-calculate the edge case comparing the first and last `timePoints`
        result = (24 * 60) - timePoints[-1] + timePoints[0]

        # Calculate the rest of the time differences, keeping the minimum value encountered
        for i in range(len(timePoints) - 1):
            result = min(result, timePoints[i + 1] - timePoints[i])
            # If a time difference of 0 is ever found, immediately return since there is no smaller value possible
            if result == 0:
                return result
        
        return result
