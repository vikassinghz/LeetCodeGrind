class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        # BRUTE FORCE APPROACH

        # if len(nums) < 0:
        #     return nums

        # Max = float('-inf')
        # for i in range(len(nums)):
        #     c_sum = 0
        #     for j in range(i, len(nums)):
        #         c_sum += nums[j]
        #         if c_sum > Max:
        #             Max = c_sum
        # return Max    

        #OPTIMAL APPROACH (KADANE'S ALGO)        
        
        C_Sum = nums[0]
        Maximum = nums[0]

        for i in range(1, len(nums)):
            
            C_Sum = max(nums[i], C_Sum + nums[i])
            Maximum = max(C_Sum, Maximum)

        return Maximum    