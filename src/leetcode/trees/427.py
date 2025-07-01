"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def dfs(row_start, col_start, n):
            value = grid[row_start][col_start]

            # Base case: the grid is size 1, and cannot be split anymore
            if n == 1:
                return Node(value, True)

            # Split the grid into 4 sub-grids and recurse
            n //= 2 # Half n to account for the split sub-grids
            top_left = dfs(row_start, col_start, n)
            top_right = dfs(row_start, col_start + n, n)
            bottom_left = dfs(row_start + n, col_start, n)
            bottom_right = dfs(row_start + n, col_start + n, n)

            # Base case: If all subgrids are leaf nodes of the same value the new node should also be a leaf node
            if (top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf
                and top_left.val == top_right.val == bottom_left.val == bottom_right.val):
                return Node(value, True)
            
            # Finally, create and return the new node
            return Node(value, False, top_left, top_right, bottom_left, bottom_right)
            
        # DFS starting in the top-left corner and recursively build the QuadTree
        return dfs(0, 0, len(grid))
