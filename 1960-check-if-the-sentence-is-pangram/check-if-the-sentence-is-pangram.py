class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        freq = {}
        count = 0

        for ch in sentence:
            if ch not in freq:
                freq[ch] = 1
                count += 1
            if ch in freq:
                pass
            elif count < 26:
                return False
        return count == 26

        