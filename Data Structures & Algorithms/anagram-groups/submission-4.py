class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - 97] += 1
            arr = tuple(arr)
            res[arr].append(s)
        
        return list(res.values())