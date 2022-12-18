> Problem: [168. Excel 表列名称](https://leetcode.cn/problems/excel-sheet-column-title/description/)

[toc]

# 思路

没啥好说的呀~

# Code

```python[]


class Solution:

    def convertToTitle(self, columnNumber: int) -> str:

        res = ''

        while columnNumber > 0:

            res = chr((columnNumber-1)%26+ord('A')) + res

            columnNumber = (columnNumber-1)//26

            print(res,columnNumber)

        return res

```
