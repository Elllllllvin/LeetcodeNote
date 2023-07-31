> Problem: [216. 组合总和 III](https://leetcode.cn/problems/combination-sum-iii/description/)

[TOC]

# 思路
> 回溯算法


# Code
```Python []

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        if k*(k+1)/2 >n:
            return res

        def dfs(res_item,i):
            if i > 10 or sum(res_item)>n:
                return
            if len(res_item) == k:ß
                if sum(res_item) == n:
                    res.append(res_item) 
                return 
            for j in range(i,10):
                dfs(res_item+[j],j+1)
        
        dfs([],1)

        return res

```
