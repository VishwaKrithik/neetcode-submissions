class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Sliding window neat

        seen = set()
        l = 0
        max_profit = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            max_profit = max(max_profit, r - l + 1)
        
        return max_profit


        # Sliding window Dirty
        """seen = set()
        l, r = 0, 0
        max_length = 0

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
            else:
                
                length = r - l
                max_length = max(max_length, length)

                # increasing left and removing from set until the duplicate element is reached
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1
                r += 1
        
        length = r - l
        max_length = max(max_length, length)

        return max_length"""