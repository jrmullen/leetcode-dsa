class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        result = 0
        l = 0
        r = 1

        # Append the first k-1 elements to the end of the array to account for a window starting at the last element
        for i in range(k - 1):
            colors.append(colors[i])

        # Sliding window over the entire array of `colors`
        for r in range(len(colors)):
            # If the
            if colors[r] == colors[r - 1]:
                l = r # Reset the window

            # The window contains `k` alternating groups -- increment the `result` counter and shift the window
            if (r - l) + 1 == k:
                result += 1 
                l += 1 # Move the left pointer forward
            
        return result
