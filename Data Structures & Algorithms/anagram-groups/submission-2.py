class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {}

        for s in strs:
            countS = "".join(sorted(s))

            if countS in res:
                res[countS].append(s)
            else:
                res[countS] = [s]
        

        return list(res.values())