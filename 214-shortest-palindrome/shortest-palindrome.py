class Solution:
    def shortestPalindrome(self, s: str) -> str:

        #Brute Force but will give time limit exceed

        # j = len(s) - 1
        # new = []

        # while j >= 0:
        #     i = 0
        #     k = j

        #     while i < k:
        #         if s[i] != s[k]:
        #             break
        #         i += 1
        #         k -= 1

        #     if i >= k:
        #         break

        #     new.append(s[j])
        #     j -= 1

        # return "".join(new) + s


        #KMP ALGO

        if not s:
            return s

        rev = s[::-1]
        temp = s + "#" + rev
        n = len(temp)
        lps = [0] * n

        j = 0
        i = 1

        while i < n:
            if temp[i] == temp[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    lps[i] = 0
                    i += 1
        lp = lps[-1]

        return rev[:len(s) - lp] + s