class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        ccount = 1
        maxc = 1
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            elif nums[i + 1] == nums[i] + 1:
                ccount += 1
            else:
                maxc = max(maxc, ccount)
                ccount = 1
        
        return max(maxc, ccount)            
        