class Solution:

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        result = []

        def dfs(node):
            # Base case: the current `node` is empty
            if not node:
                return False
            
            left = dfs(node.left) # Search the left subtree
            right = dfs(node.right) # Search the right subtree
            current = node == p or node == q # Check if the current `node` is `p` or `q`

            # Check if the current `node` is the LCA:
            # if both `left` and `right` subtrees contain `p` and `q`, the current node must be the LCA
            # if the `current` node of `p` or `q` and one of `left` or `right` also contains `p` or `q`, the current `node` must be the LCA
            if (left and right) or (current and (left or right)):
                result.append(node)
            
            # Finally, return if the current `node` subtree contains `p` or `q`
            return left or right or current
        
        dfs(root) # Traverse the tree searching for the LCA starting at the `root` node

        return result[0]
