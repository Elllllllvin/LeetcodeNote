> Problem: [58. 最后一个单词的长度](https://leetcode.cn/problems/length-of-last-word/description/)

# 思路

> 尝试一些 One-liner，，，

# Code

```Python []

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip(' ').split(' ')[-1])
```
