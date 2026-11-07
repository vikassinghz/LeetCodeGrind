class Solution:
    # def twoSum(self, numbers: list[int], target: int) -> list[int]:
    #     lt = 0
    #     rt = len(numbers) - 1
        
    #     while lt < rt:
    #         csum = numbers[lt] + numbers[rt]
    #         if csum == target:
    #             return [lt + 1, rt + 1]
    #         elif csum < target:
    #             lt += 1
    #         else:
    #             rt -= 1
    #     return []

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if tmp in mp:
                return [mp[tmp], i + 1]
            mp[numbers[i]] = i + 1
        return []
        


        