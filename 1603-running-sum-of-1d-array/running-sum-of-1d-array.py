class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        res = []
        res.append(nums[0])
        sum = nums[0]

        for i in range(1, len(nums)):
            sum += nums[i]
            res.append(sum)
        return res        