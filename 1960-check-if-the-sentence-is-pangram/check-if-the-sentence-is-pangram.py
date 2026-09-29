class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        # if len(sentence) < 26:
        #     return False

        # freq = {}

        # for ch in sentence:
        #     if ch not in freq:
        #         freq[ch] = 1

        #     if len(freq) == 26:
        #         return True

        # return count == 26
        
        char = [False] * 26
        count = 0

        for ch in sentence:
            idx = ord(ch) - ord('a')

            if not char[idx]:
                char[idx] = True
                count += 1

                if count == 26:
                    return True
        
        return count == 26


        