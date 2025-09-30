class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        # 4 pointers to track boundaries of the spiral
        left = top = 0
        right = len(matrix[0])
        bottom = len(matrix)

        while len(result) < len(matrix) * len(matrix[0]):
            
            # Right: move left -> right along the top row of the spiral
            for col in range(left, right):
                result.append(matrix[top][col])
            top += 1 # Move the top boundary down a line

            # Down: move top -> bottom along the right column of the spiral
            for row in range(top, bottom):
                result.append(matrix[row][right - 1])
            right -= 1 # Move the right boundary in a line

            # Check pointers have still not crossed
            if not (left < right and top < bottom):
                break

            # Left: move right -> left along the bottom row of the spiral
            for col in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][col])
            bottom -= 1 # Move the bottom boundary up a line

            # Up: move bottom -> top along the left column of the spiral
            for row in range(bottom - 1, top - 1, -1):
                result.append(matrix[row][left])
            left += 1 # Move the left boundary in a line
        
        return result
