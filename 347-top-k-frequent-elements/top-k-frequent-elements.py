class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # if len(nums) == 1:
        #     return nums
        # freq = {}

        # for num in nums:
        #     if num in freq:
        #         freq[num] += 1
        #     else:
        #         freq[num] = 1
        # Sfreq = sorted(freq, key = freq.get, reverse = True)
        # return Sfreq[:k]

        #OPTIMAL USING BUCKET SORT

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        