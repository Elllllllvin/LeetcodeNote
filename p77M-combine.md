> Problem: [77. 组合](https://leetcode.cn/problems/combinations/description/)

# 思路

> 回溯算法！

# 解题方法

> 经典 dfs 回溯算法，关键是剪枝处理

# Code1 我自己写的没有剪枝的

```Python []

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nums = [i+1 for i in range(n)]
        def dfs(nums,temp):
            if len(temp) == k:
                res.append(temp)
                return
            for i in range(len(nums)):
                dfs(nums[i+1:],temp+[nums[i]])
        dfs(nums,[])
        return res

```

# Code2 别人写的剪枝

```Python []

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        # DFS
        # 已取的为temp 从剩下[cur..n]区间中取或不取数 直到temp有k个元素
        def backtrack(temp,cur,n):
            # 如果加上剩下的也取不够k个（之前不取的太多了） 直接剪枝
            if len(temp) + n - cur + 1 < k:
                return

            # 如果已经取够了
            if len(temp) == k:
                result.append(temp)
                return

            #不选取当前位置  （深度优先）
            backtrack(temp,cur+1,n)

            #选取当前位置
            backtrack(temp + [cur],cur+1,n)

        backtrack([],1,n)
        return result

```
