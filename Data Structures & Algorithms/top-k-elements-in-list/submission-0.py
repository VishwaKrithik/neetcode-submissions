from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        result = []
        def maxxer(dic):
            max_val = 0
            for key, value in dic.items():
                if value > max_val:
                    idx = key
                    max_val = value
            
            z = dic.pop(idx)
            return idx
        
        for i in range(k):
            result.append(maxxer(dic))
        
        return result

            
