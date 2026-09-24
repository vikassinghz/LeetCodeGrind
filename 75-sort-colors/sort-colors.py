class Solution:
    def sortColors(self, nums: list[int]) -> None:
        
        Low = 0
        Mid = 0
        High = len(nums) - 1

        while Mid <= High:

            if nums[Mid] == 0:
                nums[Mid], nums[Low] = nums[Low], nums[Mid]
                Low += 1
                Mid += 1

            elif nums[Mid] == 1:
                Mid += 1

            elif nums[Mid] == 2:
                nums[Mid], nums[High] = nums[High], nums[Mid]
                High -= 1

        return nums           

