class Solution:
    def reverseBits(self, n: int) -> int:
        
        s = 0
        n = f"{n:032b}"
        return int(n[::-1], 2)

        # for _ in range(32):
        #     s &= (n & 1)
        #     print(s)
        #     n >>= 1
        #     s <<= 1
        
        # print(s)
        # return s