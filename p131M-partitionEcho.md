> Problem: [131. 分割回文串](https://leetcode.cn/problems/palindrome-partitioning/description/)

# 思路

> 经典 dfs+回溯算法

# 解题方法

> 小技巧:把 path 更新放到参数传递中去，可以直接达到回溯的效果，不用等 dfs 之后再去特意恢复 path。

# Code

```Python3 []

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(temps,path):
            if len(temps) == 0:
                res.append(path)
            for i in range(1,len(temps)+1):
                if temps[:i] == temps[:i][::-1]:
                    dfs(temps[i:],path+[temps[:i]])
        dfs(s,[])
        return res
```
