# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         seen = {}

#         for char in s:
#             if char in seen:
#                 seen[char] += 1
#             else:
#                 seen[char] = 1

#         for char in t:
#             if char not in seen:
#                 return False
#             seen[char] -= 1

#             if seen[char] < 0:
#                 return False
#         return True

class Solution:
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for num in count:
            if num != 0:
                return False

        return True

        