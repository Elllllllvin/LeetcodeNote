> Problem: [242. 有效的字母异位词](https://leetcode.cn/problems/valid-anagram/description/)

[TOC]

# 思路
> 哈希表

# 复杂度
- 时间复杂度:  $O(n)$

- 空间复杂度:  $O(n)$

# Code
```Python []

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
        for char in t:
            if char not in dic or dic[char]==0:
                return False
            else:
                dic[char] -= 1
        
        if sum(dic.values()) != 0:
            return False
        else:
            return True

            
```
