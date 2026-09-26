import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles) + 1

        soln = 1

        while left <= right:
            k = (left + right) // 2

            time = 0
            for num in piles:
                if time >= h:
                    time += 1
                    break
                
                time += math.ceil(num / k)
            
            if time <= h:
                soln = k
                right = k - 1
            else:
                left = k + 1

        return soln





        for k in range(1, max(piles) + 1):
            time = 0
            for num in piles:
                if time >= h:
                    time += 1 
                    break
                time += math.ceil(num / k)
            
            if time <= h:
                return k
        
        return -1