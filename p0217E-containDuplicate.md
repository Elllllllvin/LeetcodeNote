> Problem: [217. 存在重复元素](https://leetcode.cn/problems/contains-duplicate/description/)

[TOC]

# 思路
> hash表，利用字典

# 复杂度
- 时间复杂度: $O(n)$

- 空间复杂度:  $O(n)$

# Code1
```Python []

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l = {}
        for item in nums:
            if item not in l.keys():
                l[item] = 1
            else:
                return True
        
        return False

```

# Code2 Set
利用set()去重来解决
