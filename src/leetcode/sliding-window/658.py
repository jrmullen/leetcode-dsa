class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # First, binary search to find the index of closest element to `x`
        l = 0
        r = len(arr) - 1
        target_idx = 0 # Track the closest index of the array to `x`

        while l < r:
            mid = (l + r) // 2
            if arr[mid] < x:
                l = mid + 1 # Eliminate everything to the left
            else:
                r = mid # Elemenate everything to the right
            target_idx = l # Update the `target_idx` pointer with the left pointer value
        
        # Next, starting from the `target_idx`, build a window containing the `k` closest elements
        l = target_idx - 1
        r = target_idx
        while r - l - 1 < k:
            if r >= len(arr): # Edge cases: stay within the bounds of the array
                l -= 1
            elif l < 0:
                r += 1
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                l -= 1 # If the left value's distance is closer or equal, expand the window to the left
            else:
                r += 1 # If the right value's distance is closer, expand the window to the right
        
        # Return the window
        return arr[l + 1:r]
