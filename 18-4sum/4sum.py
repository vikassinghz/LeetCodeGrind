class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                lt = j + 1
                rt = n - 1

                while lt < rt:
                    tsum = nums[i] + nums[j] + nums[lt] + nums[rt]

                    if tsum == target:
                        res.append([nums[i], nums[j], nums[lt], nums[rt]])
                        lt += 1
                        rt -= 1
                    
                        while lt < rt and nums[lt] == nums[lt - 1]:
                            lt += 1
                        while lt < rt and nums[rt] == nums[rt + 1]:
                            rt -= 1
                    elif tsum < target:
                        lt += 1
                    else:
                        rt -= 1
        return res