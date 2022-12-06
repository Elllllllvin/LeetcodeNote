> Problem: [130. 被围绕的区域](https://leetcode.cn/problems/surrounded-regions/description/)

# 思路

> 一道很新的 dfs

# 复杂度

- 时间复杂度: $O(m*n)$

- 空间复杂度: $O(m*n)$ 主要为深度优先搜索的栈的开销。

# Code

```Python []

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board),len(board[0])

        def dfs(x,y):
            if not 0<=x<m or not 0<=y<n or board[x][y] != 'O':
                return
            board[x][y] = 'A'
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y+1)
            dfs(x,y-1)

        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        for j in range(n):
            dfs(0,j)
            dfs(m-1,j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    continue
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'

```
