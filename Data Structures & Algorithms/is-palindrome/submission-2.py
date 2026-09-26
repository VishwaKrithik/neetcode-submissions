class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        else:
            return True

















        # l = 0
        # r = len(s) - 1

        # while l < r:
        #     while l < r and not s[l].isalnum():
        #         l += 1
        #     while r > l and not s[r].isalnum():
        #         r -= 1
        #     if s[l].lower() != s[r].lower():
        #         return False
        #     l, r = l + 1, r - 1
        
        # return True

        """while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
        return True"""