> Problem: [36. 有效的数独](https://leetcode.cn/problems/valid-sudoku/description/)

[TOC]

# 思路

> 分开判断三个条件+散列表思想，只需遍历一遍

# 复杂度

- 时间复杂度: $O(n^2)$

- 空间复杂度: $O(n^2)$

# Code

```Python []

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        flag_row = True
        flag_col = True
        flag_sqr = True
        flag = flag_col and flag_row and flag_sqr
        sqr = [[0]*9 for i in range(9)]
        col = [[0]*9 for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    if board[i].count(board[i][j])>1:
                        flag_row = False
                        break
                    t = int(board[i][j])-1
                    if col[j][t] > 0:
                        flag_col = False
                        break
                    else:
                        col[j][t] += 1

                    if sqr[(i//3)*3+j//3][t] > 0:
                        flag_sqr = False
                        break
                    else:
                        sqr[(i//3)*3+j//3][t] += 1
            flag = flag_col and flag_row and flag_sqr
            if flag == False:
                break
        return flag
```
