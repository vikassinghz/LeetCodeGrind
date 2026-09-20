class Solution:
    def mirrorFrequency(self, s: str) -> int:
        freq = {}
        res = 0
        visited = set()

        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        for char in freq:
            if char in visited:
                continue

            if 'a' <= char <= 'z':
                mirror = chr(ord('a') + ord('z') - ord(char))
            else:
                mirror = chr(ord('0') + ord('9') - ord(char))

            if mirror in freq:
                res += abs(freq[char] - freq[mirror])
            else:
                res += freq[char]

            visited.add(char)
            visited.add(mirror)

        return res
        