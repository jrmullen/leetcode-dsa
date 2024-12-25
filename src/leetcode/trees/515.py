# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        # Base case: if there is no `root` node, return immediately
        if not root:
            return result
        
        q = deque([root])

        # Standard BFS level-order traversal
        while q:
            # Track the largest value encountererd at each level
            largest = float('-inf')
            for _ in range(len(q)):
                node = q.pop()
                largest = max(largest, node.val)

                # Add children to the `q`
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)

            # Finally, append the largest value to the `result` list
            result.append(largest)
        
        return result
