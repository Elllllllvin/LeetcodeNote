> Problem: [40. 组合总和 II](https://leetcode.cn/problems/combination-sum-ii/description/)

# Code

```Python []
又回溯。。。。。。。。。。
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates,start,res,path,target):
            if target<0  :
                return []
            elif target == 0:
                if path not in res:
                    res.append(path)
                return
            else:
                for i in range(start,len(candidates)):
                    if(candidates[start]>target):
                        return
                    if(i>start and candidates[i-1]==candidates[i]):
                        continue
                    dfs(candidates,i+1,res,path + [candidates[i]],target-candidates[i])

        candidates.sort()
        res = []
        path = []
        dfs(candidates,0,res,path,target)
        return res
```
