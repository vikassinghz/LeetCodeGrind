class Solution:
    def compress(self, chars: list[str]) -> int:
        j = 0
        c = 1

        for i in range(len(chars)):
            if i == len(chars) - 1 or chars[i] != chars[i + 1]:
                chars[j] = chars[i]
                j += 1

                if c > 1:
                    for k in str(c):
                        chars[j] = k
                        j += 1
                
                c = 1
            else:
                c += 1
        return j
