# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node):
            # Base case: if there is no node, return a new node with the given `val` to be inserted as a leaf
            if not node:
                return TreeNode(val)
            
            # BST: values in the left subtree must be less than the root node's value
            # values in the right subtree must be greater than the root node.
            #
            # Traverse the tree until a node is found that has no leaf, then insert a new node
            if val < node.val:
                node.left = dfs(node.left)
            else:
                node.right = dfs(node.right)
            
            # Finally return the node
            return node
        
        # Recursively DFS until the `val` is inserted, then return the root node
        return dfs(root)
