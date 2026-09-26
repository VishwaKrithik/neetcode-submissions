class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        words = set(wordDict)

        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        min_len = min(len(w) for w in wordDict)
        max_len = max(len(w) for w in wordDict)

        for i in range(min_len, n + 1):
            for length in range(min_len, min(i, max_len) + 1):
                prev_idx = i - length
                if dp[prev_idx] and s[prev_idx:i] in words:
                    dp[i] = True
                    break
        
        return dp[-1]