class Solution:
    #USING DP HashSet and HashMap
    #OPTIMAL

    def isConcatenated(self, word, hs, hm):
        if word in hm:
            return hm[word]
        
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]

            if prefix in hs:
                if suffix in hs or self.isConcatenated(suffix, hs, hm):
                    hm[word] = True
                    return True
        hm[word] = False
        return False

    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        hs = set()
        
        for word in words:
            hs.add(word)

        hm = {}
        res = []

        for word in words:
            if self.isConcatenated(word, hs, hm):
                res.append(word)
        return res     