> Problem: [289. 生命游戏](https://leetcode.cn/problems/game-of-life/description/)

[TOC]

# 思路
题目不难，但好好体会访问邻居的方法！！

# 解题方法
> 描述你的解题方法

# 复杂度
- 时间复杂度:  $O(mn)$

- 空间复杂度:  $O(mn)$

# Code
```Python []

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board),len(board[0])
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        # 从原数组复制一份到 copy_board 中
        copy_board = [[board[i][j] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                neighborAlive = 0
                for neighbor in neighbors:
                    ti  = i + neighbor[0]
                    tj  = j + neighbor[1]
                    if 0 <= ti < m and 0 <= tj < n and copy_board[ti][tj] == 1:
                        neighborAlive += 1
                
                if copy_board[i][j] == 1 and neighborAlive<2:
                    board[i][j] = 0
                if copy_board[i][j] == 1 and neighborAlive>3:
                    board[i][j] = 0
                if copy_board[i][j] == 0 and neighborAlive == 3:
                    board[i][j] = 1
                
                
```
