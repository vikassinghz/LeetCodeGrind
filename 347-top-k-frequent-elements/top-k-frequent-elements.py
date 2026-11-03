class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if len(nums) == 1:
            return nums
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        Sfreq = sorted(freq, key = freq.get, reverse = True)
        return Sfreq[:k]

        