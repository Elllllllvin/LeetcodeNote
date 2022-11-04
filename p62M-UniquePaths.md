> Problem: [62. 不同路径](https://leetcode.cn/problems/unique-paths/description/)

# 思路

> 纯数学方法

# Code

```Python3 []

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = 1
        s = m+n-2
        for i in range(min(m-1,n-1)):
            res = res*s//(i+1)
            s -= 1

        return res
```
