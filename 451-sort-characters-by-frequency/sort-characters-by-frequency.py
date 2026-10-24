class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        sorted_chars = sorted(freq, key=lambda x: freq[x], reverse=True)

        ans = ""
        for ch in sorted_chars:
            ans += ch * freq[ch]

        return ans
        