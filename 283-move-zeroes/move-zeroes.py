class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        temp = 0
        for i in range (len(nums)):
            if nums[i] != 0:
                nums[temp], nums[i] = nums[i], nums[temp]
                temp += 1