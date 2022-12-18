> Problem: [78. 子集](https://leetcode.cn/problems/subsets/description/)

# 思路

> 回溯！！回溯!!!

# Code1 哥的回溯（永远不如别人的，，，）

```Python []
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(temp,i):
            if temp not in res:
                res.append(temp)
            if i == n:
                return
            dfs(temp,i+1)
            dfs(temp+[nums[i]],i+1)
        dfs([],0)
        return res
```

# Code2 别人优化的回溯

```Python []

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(temp,start):
            res.append(temp)
            if start == n:
                return
            for i in range(start,n):
                dfs(temp+[nums[i]],i+1)
        dfs([],0)
        return res


```
