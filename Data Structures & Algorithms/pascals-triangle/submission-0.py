class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]

        dp = [[1], [1, 1]]

        if numRows == 2:
            return dp

        for i in range(2, numRows):
            temp = [1]
            # print(dp)
            for j in range(1, i):
                temp.append(dp[i - 1][j - 1] + dp[i - 1][j])
            temp.append(1)
            dp.append(temp)

        # print(dp)

        return dp