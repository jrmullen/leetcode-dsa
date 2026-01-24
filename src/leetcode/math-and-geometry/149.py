class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        result = 0

        # Base case: a single point will always be the maximum
        if N == 1:
            return 1

        # Iterate over distinct point pairs
        for i in range(N - 1):
            x1, y1 = points[i]
            slopes = defaultdict(int) # { slope: count } - keep in mind Float type could potentially cause accuracy issues with certain inputs

            for j in range(i + 1, N):
                x2, y2 = points[j]

                # Compare the X-axis coordinate to avoid dividing by 0
                if x1 == x2:
                    slope = float('INF')
                else:
                     slope = (y2 - y1) / (x2 - x1) # Calculate the slope between the two points: rise / run
                
                slopes[slope] += 1 # Points that share the same slope should share the same line
                result = max(result, slopes[slope] + 1) # Track the largest number of points that share the same line
                
        return result
