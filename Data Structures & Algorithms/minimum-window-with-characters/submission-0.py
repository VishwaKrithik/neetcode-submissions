class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        len_s, len_t = len(s), len(t)

        if len_s < len_t or not s or not t:
            return ""
        
        target_count = Counter(t)
        window_count = {}

        have, need = 0, len(target_count)
        res_len = float("inf")
        res_bounds = [-1, -1]

        l = 0
        for r in range(len(s)):
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1

            if char in target_count and window_count[char] == target_count[char]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res_len = r - l + 1
                    res_bounds = [l, r]
                
                left_char = s[l]
                window_count[left_char] -= 1
                if left_char in target_count and window_count[left_char] < target_count[left_char]:
                    have -= 1
                l += 1
            
        l, r = res_bounds
        return s[l:r + 1] if res_len != float("inf") else ""