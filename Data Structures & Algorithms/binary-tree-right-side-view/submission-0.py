# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        dq = deque()
        dq.append(root)
        ans = []
        while dq:
            level = []
            for i in range(len(dq)):
                node = dq.popleft()
                if node:
                    level.append(node.val)
                    dq.append(node.left)
                    dq.append(node.right)

            if level:
                ans.append(level[-1])
        
        return ans