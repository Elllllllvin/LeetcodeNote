> Problem: [39. 组合总和](https://leetcode.cn/problems/combination-sum/description/)

回溯算法：dfs 深度优先！！！

# Code

```Python []

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #添加start进行剪枝操作，时间快了很多
        #因为在添加2作为path后，之后的不用在考虑2，因此达到剪枝操作
        def dfs(candidates,target,res,path,start):
            if target < 0:
                return []
            if target == 0:
                res.append(path)
                return
            for i in range(start,len(candidates)):
                dfs(candidates,target-candidates[i],res,[candidates[i]]+path,i)

        path = []
        res = []
        dfs(candidates,target,res,path,0)

        return res

```
