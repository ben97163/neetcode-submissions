# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = deque()
        dq.append(root)
        ans = []
        while dq:
            q = len(dq)
            level = []
            for i in range(q):
                cur = dq.popleft()
                if cur:
                    dq.append(cur.left) 
                    dq.append(cur.right)
                    level.append(cur.val)
            if level:
                ans.append(level)
        
        return ans