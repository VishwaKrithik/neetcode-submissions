class Solution:
    def countBits(self, n: int) -> List[int]:
        
        arr = [0] * (n + 1)

        for num in range(n + 1):
            arr[num] = bin(num).count('1')
        
        return arr