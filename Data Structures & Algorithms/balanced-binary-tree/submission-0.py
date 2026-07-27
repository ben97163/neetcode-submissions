# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root: return (True, 0)

            left_b, left_h = dfs(root.left)
            right_b, right_h = dfs(root.right)

            balanced = left_b and right_b and abs(left_h - right_h) <= 1
            height = 1 + max(left_h, right_h)
            return (balanced, height)
        
        return dfs(root)[0]

    