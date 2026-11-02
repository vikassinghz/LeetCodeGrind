class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False