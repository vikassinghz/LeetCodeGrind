class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:

        res = []
        if len(s) < 4 or len(s) > 12:
            return res
        
        def backtrack(start, parts):
            if len(parts) == 4:
                if start == len(s):
                    res.append(".".join(parts))
                return
            
            for length in range(1, 4):
                if start + length > len(s):
                    break
                
                segment = s[start: start + length]

                if len(segment) > 1 and segment[0] == '0':
                    break
                if int(segment) <= 255:
                    backtrack(start + length, parts + [segment])
        backtrack(0, [])
        return res
