class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # if not nums:
        #     return 0
        
        # nums.sort()
        # ccount = 1
        # maxc = 1
        
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         continue
        #     elif nums[i + 1] == nums[i] + 1:
        #         ccount += 1
        #     else:
        #         maxc = max(maxc, ccount)
        #         ccount = 1
        
        # return max(maxc, ccount)            
        
        #OPTIMAL APPROACH USIGN HASH SET

        hashset = set(nums)
        maxc = 0

        for num in hashset:
            if num - 1 not in hashset:
                count = 1

                while num + count in hashset:
                    count += 1

                maxc = max(maxc, count)

        return maxc