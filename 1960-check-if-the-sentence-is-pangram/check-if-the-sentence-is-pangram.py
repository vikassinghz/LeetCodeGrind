class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        if len(sentence) < 26:
            return False

        freq = {}

        for ch in sentence:
            if ch not in freq:
                freq[ch] = 1

            if len(freq) == 26:
                return True

        return count == 26

        