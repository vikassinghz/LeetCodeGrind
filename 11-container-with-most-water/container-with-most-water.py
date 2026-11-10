class Solution:
    def maxArea(self, height: list[int]) -> int:
        lt, rt = 0, len(height) - 1
        res = 0
        while lt < rt:
            area = min(height[lt], height[rt]) * (rt - lt)
            res = max(res, area)
            if height[lt] <= height[rt]:
                lt += 1
            else:
                rt -= 1
        return res
                
        