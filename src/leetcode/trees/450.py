# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Base case: the current root does not exist
        if not root:
            return root
        
        # Recursively traverse the BST until the target node is found or the bottom of the tree is reached
        if root.val < key:
            root.right = self.deleteNode(root.right, key) # If the value is lower, traverse the left sub-tree
        elif root.val > key:
            root.left = self.deleteNode(root.left, key) # If the value is greater, traverse the right sub-tree
        else: # The target node has been reached

            # If there is only 1 child, that child can be returned immediately
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            
            # Otherwise, find the smallest child node of the right subtree
            current = root.right
            while current.left:
                current = current.left
            
            # Update the value of the root node with the smallest value from the right sub-tree
            root.val = current.val

            # Recurse on the right subtree to replace all child nodes
            root.right = self.deleteNode(root.right, root.val)
        
        # Finally, return the root node
        return root
