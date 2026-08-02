class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        max_left = 0
        for i in range(len(height)):
            maxLeft[i] = max_left
            if height[i] > max_left:
                max_left = height[i]
        maxRight = [0] * len(height)
        max_right = 0
        for i in range(len(height) - 1 , -1, -1):
            maxRight[i] = max_right
            if height[i] > max_right:
                max_right = height[i]
        
        ans = 0
        for i in range(len(height)):
            ans += max(0, min(maxLeft[i], maxRight[i]) - height[i])
        
        return ans
