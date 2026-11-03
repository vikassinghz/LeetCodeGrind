class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        res = {}

        for s in strs:
            SS = "".join(sorted(s))
            if SS in res:
                res[SS].append(s)
            else:
                res[SS] = [s]
        return list(res.values())
        