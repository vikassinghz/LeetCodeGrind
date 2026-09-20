class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        freq = {}
        res = 0

        for nums in str(n):
            nums = int(nums)
            if nums in freq:
                freq[nums] += 1
            else:
                freq[nums] = 1
        for nums in freq:
            nums = nums * freq[nums]
            res += nums
        return res    

        