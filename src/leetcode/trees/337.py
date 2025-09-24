# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        # Recursively calculate the sum for both scenarios: rob or do not rob the node.
        # Return the totals as a tuple [robbed, not_robbed]
        def dfs(node):
            # Base case: there is no root node
            if not node:
                return [0, 0]
            
            left = dfs(node.left) # Calculate the left subtree
            right = dfs(node.right) # Calculate the right subtree

            # If the current node is robbed, neither of its children may be robbed
            robbed = node.val + left[1] + right[1]

            # If the current node is NOT robbed, both of its children may be robbed
            not_robbed = max(left) + max(right) # Take the largest value for each

            return [robbed, not_robbed] # Return the results
        
        # DFS starting at the root to get the totals for each scenario: rob or do not rob the root
        robbed, not_robbed = dfs(root)

        return max(robbed, not_robbed) # Return whichever value is larger
