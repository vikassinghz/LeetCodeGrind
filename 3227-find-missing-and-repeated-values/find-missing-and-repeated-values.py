class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total_number = n * n
        xor_all = 0

        for row in grid:
            for num in row:
                xor_all ^= num

        for i in range(1, total_number + 1):
            xor_all ^= i

        mask = xor_all & -xor_all
        first_group = 0
        second_group = 0

        for row in grid:
            for num in row:
                if num & mask:
                    first_group ^= num
                else:
                    second_group ^= num

        for i in range(1, total_number + 1):
            if i & mask:
                first_group ^= i
            else:
                second_group ^= i

        for row in grid:
            if first_group in row:
                return [first_group, second_group]
        
        return [second_group, first_group]
        