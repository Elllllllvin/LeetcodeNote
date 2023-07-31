> Problem: [290. 单词规律](https://leetcode.cn/problems/word-pattern/description/)

[TOC]

# 思路
双向哈希表

# Code
```Python []

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ch2word = dict()
        word2ch = dict()
        l = s.split(' ')
        if len(l)!= len(pattern):
            return False
        for ch,word in zip(pattern,l):
            if (ch in ch2word and ch2word[ch]!= word )or (word in word2ch and word2ch[word]!= ch):
                return False
            word2ch[word] = ch
            ch2word[ch] = word
        return True            

```
