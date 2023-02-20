> Problem: [171. Excel 表列序号](https://leetcode.cn/problems/excel-sheet-column-number/description/)

[TOC]

# 思路

没啥好说的

# Code

```Python []

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i in range(len(columnTitle)):
            res = res*26 + ord(columnTitle[i])-ord('A')+1
        return res
```
