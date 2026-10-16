class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        prev = 0
        nxt = 0
        res = 0
        row = len(bank)
        col = len(bank[0])

        for i in range(row):
            for j in range(col):
                if bank[i][j] == '1':
                    nxt += 1
            if prev != 0 and nxt != 0:
                res += prev * nxt
            if nxt != 0:
                prev = nxt
                nxt = 0
        return res
        