> Problem: [47. 全排列 II](https://leetcode.cn/problems/permutations-ii/description/)

# 思路

> 回溯算法 + 剪枝

# 复杂度

- 时间复杂度: $O(n × n!)$

- 空间复杂度: $O(n)$
  > res 需要$O(n)$，递归栈需要$O(n)$

# Code

```Python3 []

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums,temp):
            if len(nums) == 0 and temp not in res:
                res.append(temp)
                return
            for j in range(len(nums)):
                if (j>0 and nums[j] == nums[j-1]):
                    continue
                else:
                    backtrack(nums[:j]+nums[j+1:],temp+[nums[j]])
        nums.sort()
        backtrack(nums,[])

        return res

```
