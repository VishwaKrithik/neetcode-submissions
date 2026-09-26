import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        res = [[] for _ in range(len(nums) + 1)]

        for num, cnt in count.items():
            res[cnt].append(num)
        
        ans = []

        for i in range(len(res) - 1, -1, -1):
            for num in res[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
    
