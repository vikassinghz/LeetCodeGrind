class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        lt = 0
        rt = len(numbers) - 1
        
        while lt < rt:
            csum = numbers[lt] + numbers[rt]
            if csum == target:
                return [lt + 1, rt + 1]
            elif csum < target:
                lt += 1
            else:
                rt -= 1
        return []
        


        