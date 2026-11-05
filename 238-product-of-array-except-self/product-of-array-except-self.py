class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        # OPTIMAL APPROACH USING PREFIX SUFFIX
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res

        # res = []
        # prd = 1
        # zero = nums.count(0)

        # for num in nums:
        #     if num != 0:
        #         prd *= num

        # if zero > 1:
        #     return [0] * len(nums)

        # if zero == 1:
        #     for num in nums:
        #         if num == 0:
        #             res.append(prd)
        #         else:
        #             res.append(0)
        #     return res

        # for num in nums:
        #     res.append(prd // num)

        # return res
        