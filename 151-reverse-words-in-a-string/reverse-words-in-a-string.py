class Solution:
    def reverseWords(self, s: str) -> str:
        char = list(s)
        n = len(char)

        def rev_range(arr, left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        rev_range(char, 0, n - 1)

        j = 0
        i = 0

        while i < n:
            if char[i] != " ":

                if j != 0:
                    char[j] = " "
                    j += 1
                
                start = j

                while i < n and char[i] != " ":
                    char[j] = char[i]
                    j += 1
                    i += 1

                rev_range(char, start, j - 1)
            i += 1

        return "".join(char[:j])
        