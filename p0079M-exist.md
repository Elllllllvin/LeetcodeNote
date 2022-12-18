> Problem: [79. 单词搜索](https://leetcode.cn/problems/word-search/description/)

# 思路

回溯！！！回溯！！

我发现只要讨论里有人说这是 xxx 面试题，我就会努力做出来，要没人说就看看题解过去了。。

# Code

```Python []

import copy
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board),len(board[0])
        length = len(word)
        flag = False

        def dfs(tempboard,cur,i,j):
            if cur != length and(i<0 or i>=m or j<0 or j>=n):
                return False
            if cur == length:
                return True
            if tempboard[i][j] == '_':
                return False
            t = tempboard[i][j]
            if tempboard[i][j] == word[cur]:
                tempboard[i][j] = '_'
                flag = dfs(tempboard,cur+1,i,j+1) or dfs(tempboard,cur+1,i+1,j) or dfs(tempboard,cur+1,i,j-1) or dfs(tempboard,cur+1,i-1,j)
                if flag == True:
                    return flag
                else:
                    tempboard[i][j] = t #回溯keypoint
                    return False
            else:
                return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    flag = dfs(board,0,i,j)
                    if flag == True:
                        return flag
        return flag

```
