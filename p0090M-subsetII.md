> Problem: [90. 子集 II](https://leetcode.cn/problems/subsets-ii/description/)

# Code1 dfs 但是很慢

```Python []

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(pos,temp):
            if temp not in res:
                res.append(temp)
            if len(nums) == pos:
                return
            for i in range(pos,len(nums)):
                dfs(i+1,temp+[nums[i]])
        dfs(0,[])
        return list(res)

```

# Code2 dfs 优化一下吧

```Python []
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(pos,temp):
            if temp not in res:
                res.append(temp)
            if len(nums) == pos:
                return
            for i in range(pos,len(nums)):
                if i>pos and nums[i]==nums[i-1]:
                    continue #这里剪一下枝！
                dfs(i+1,temp+[nums[i]])
        dfs(0,[])
        return res
```
