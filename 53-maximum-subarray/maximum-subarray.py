class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        C_Sum = nums[0]
        Maximum = nums[0]

        for i in range(1, len(nums)):
            
            C_Sum = max(nums[i], C_Sum + nums[i])
            Maximum = max(C_Sum, Maximum)

        return Maximum    