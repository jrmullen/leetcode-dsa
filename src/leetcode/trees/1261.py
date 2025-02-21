# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.visited = set()
        root.val = 0 # Set the `root` node's default value to be 0
        self.dfs(root) # DFS starting at the `root` node to re-populate the tree
    
    def dfs(self, node):
        # Base case
        if not node:
            return
        
        # Add the node's value to the `visited` set
        self.visited.add(node.val)

        # Traverse the left child tree
        if node.left:
            node.left.val = 2 * node.val + 1
            self.dfs(node.left)
        
        # Traverse the right child tree
        if node.right:
            node.right.val = 2 * node.val + 2
            self.dfs(node.right) 

    def find(self, target: int) -> bool:
        # Search for the `target` in the `visited` HashSet
        return target in self.visited

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
