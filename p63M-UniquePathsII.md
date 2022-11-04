> Problem: [63. 不同路径 II](https://leetcode.cn/problems/unique-paths-ii/description/)

# 复杂度

- 时间复杂度: $O(mn)$

- 空间复杂度: $O(1)$

# Code

```Python []

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        for i in range(1,m):
            if obstacleGrid[i][0] == 1 or obstacleGrid[i-1][0] == 0 :
                obstacleGrid[i][0] = 0
            else:
                obstacleGrid[i][0] = obstacleGrid[i-1][0]
        for i in range(1,n):
            if obstacleGrid[0][i] == 1 or obstacleGrid[0][i-1] == 0 :
                obstacleGrid[0][i] = 0
            else:
                obstacleGrid[0][i] = obstacleGrid[0][i-1]
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] != 1:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
        # print(obstacleGrid)
        return obstacleGrid[m-1][n-1]


```
