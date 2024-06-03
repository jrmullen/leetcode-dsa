# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sort = []

        # DFS in-order traversal -> Left, Root, Right
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            sort.append(node.val)  # Visiting nodes in-order results in a sorted array of values smallest -> largest
            dfs(node.right)

        dfs(root)
        return sort[k - 1]  # Return the Kth element
