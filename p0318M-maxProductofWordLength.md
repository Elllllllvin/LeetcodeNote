> Problem: [318. 最大单词长度乘积](https://leetcode.cn/problems/maximum-product-of-word-lengths/description/)

[TOC]

# 思路
> 经典的位运算！

# 解题方法
> 描述你的解题方法

# 复杂度
- 时间复杂度: $O(n^2 + L)$，其中L是所有单词长度和

- 空间复杂度: $O(n)$

# Code
```Python []

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        binword = [(0,0) for _ in range(n)]
        for i,word in enumerate(words):
            tmpbin = 0
            for ch in word:
                shift = 1 << ord(ch) - ord('a')
                if shift & tmpbin == 0:
                    tmpbin += shift
            binword[i] = (len(word),tmpbin)
        res = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if binword[i][1] & binword[j][1] == 0:
                    res = max(res,binword[i][0]*binword[j][0])
        
        return res

            
            



```
