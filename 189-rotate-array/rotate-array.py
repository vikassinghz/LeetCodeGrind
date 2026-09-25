class Solution:
    def rotate(self, nums: list[int], k: int) -> None:

        #Brute Force

        # while k > 0:
        #     k -= 1
        #     val = nums[len(nums) - 1]

        #     for i in range(len(nums) - 1, 0, -1):
        #         nums[i] = nums[i - 1]
        #     nums[0] = val

        # return nums    

        #Optimal
        k = k % len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        return nums

