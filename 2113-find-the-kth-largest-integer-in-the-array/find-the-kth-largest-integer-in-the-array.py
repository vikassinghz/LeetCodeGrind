class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:

        nums.sort(key = int, reverse = True)

        return nums[k - 1]        