> Problem: [165. 比较版本号](https://leetcode.cn/problems/compare-version-numbers/description/)

# 思路

> 字符串分割没啥好说的

# Code

```Python []

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        L1 = version1.split('.')
        L2 = version2.split('.')
        if len(L1) < len(L2):
            L1 = L1 + [0]*(len(L2)-len(L1))
        else:
            L2 = L2 + [0]*(len(L1)-len(L2))

        for i in range(len(L1)):
            if int(L1[i])<int(L2[i]):
                return -1
            elif int(L1[i]) > int(L2[i]):
                return 1

        return 0
```
