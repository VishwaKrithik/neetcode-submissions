class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = 0

        for i in range(26):
            ch = chr(ord('a') + i)

            first = s.find(ch)
            last = s.rfind(ch)

            if first != -1 and first < last:
                count += len(set(s[first + 1:last]))

        return count