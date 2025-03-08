class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Sliding window technique: track the minimum number of white blocks within each window
        result = float('inf')
        white = 0
        l = 0

        # Iterate over each block from left to right
        for r in range(len(blocks)):
            white += 1 if blocks[r] == 'W' else 0 # If the newly added block is white, increment the `white` counter

            # If the window is of size `k`
            if (r - l) + 1 == k:
                result = min(result, white) # Compare the number of `white` blocks within the window with the lowest seen
                white -= 1 if blocks[l] == 'W' else 0 # If a white block will be ejected from the window, decrease the counter
                l += 1 # Shift the left pointer forward to shrink the window
        
        return result
