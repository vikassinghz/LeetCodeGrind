class Solution:
    #Brute Approach

    def longestDupSubstring(self, s: str) -> str:
    #     n = len(s)
    #     res = ""

    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             length = 0

    #             while (i + length < n and
    #                    j + length < n and
    #                    s[i + length] == s[j + length]):
    #                 length += 1

    #             if length > len(res):
    #                 res = s[i:i + length]

    #     return res


        n = len(s)
        base = 26
        mod = 2**61 - 1

        nums = [ord(c) - ord('a') for c in s]

        def search(length):
            power = pow(base, length, mod)
            h = 0
            seen = set()

            for i in range(length):
                h = (h * base + nums[i]) % mod

            seen.add(h)

            for i in range(length, n):
                h = (h * base - nums[i - length] * power
                     + nums[i]) % mod

                if h in seen:
                    start = i - length + 1
                    return start

                seen.add(h)

            return -1

        left, right = 1, n - 1
        start = -1
        best = 0

        while left <= right:
            mid = (left + right) // 2
            idx = search(mid)

            if idx != -1:
                start = idx
                best = mid
                left = mid + 1
            else:
                right = mid - 1

        return s[start:start + best] if best else ""