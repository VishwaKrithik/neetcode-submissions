class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Round 2
        dick = {}
        cunt = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            dick[num] = 1 + dick.get(num, 0)
        
        for key, val in dick.items():
            cunt[val].append(key)
        
        res = []
        for i in range(len(cunt) - 1, -1 ,-1):
            for val in cunt[i]:
                res.append(val)
                if len(res) == k:
                    return res





        
        # dic = {}
        # freq = [[] for _ in range(len(nums) + 1)]

        # for n in nums:
        #     dic[n] = 1 + dic.get(n, 0)
        # for key, value in dic.items():
        #     freq[value].append(key)
        
        # res = []    
        # for i in range(len(freq) - 1, 0, -1):
        #     for j in freq[i]:
        #         res.append(j)
        #         if len(res) == k:
        #             return res
        # return 
        
        """dic = Counter(nums)
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
        
        return result"""

            
