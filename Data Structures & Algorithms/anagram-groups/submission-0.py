class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = {}

        for s in strs:
            elt = "".join(sorted(s))

            if elt in ans:
                ans[elt].append(s)
            else:
                ans[elt] = [s]
        
        return list(ans.values())