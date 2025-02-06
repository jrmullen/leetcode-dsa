class Solution:
    def trap(self, height: List[int]) -> int:
        # Base case
        if not height:
            return 0

        # Two pointers - start at the outside of the list and move inward
        l = 0
        r = len(height) - 1

        # Track the maximum height on each side of the list
        maxLeft = height[l]
        maxRight = height[r]
        
        result = 0
        while l < r:
            if maxLeft < maxRight:
                l += 1 # Move the left pointer inward and update the `maxLeft`
                maxLeft = max(maxLeft, height[l])
                # The water will be `maxLeft` units deep. To account for the ground underneath, subtract the `height`
                area = maxLeft - height[l]
                if area > 0: # Update the `area` to account for the new area of water
                    result += area
            else:
                r -= 1 # Move the right pointer inward and update the `maxRight`
                maxRight = max(maxRight, height[r])
                area = maxRight - height[r]
                if area > 0:
                    result += area
        
        return result
