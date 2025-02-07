class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        result = []
        balls = {} # Track the colors of the balls that are painted
        colors = defaultdict(int) # Track the number of active colors

        # Iterate over each query
        for ball, color in queries:
            # Decrement the previous color in the `colors` map
            prev = balls[ball] if ball in balls else 0
            if prev != 0 and colors[prev]:
                if colors[prev] == 1:
                    del colors[prev]
                else:
                    colors[prev] -= 1
            
            # Apply the new color to the ball
            balls[ball] = color
            colors[color] += 1

            # Update the results
            result.append(len(colors))

        return result
