> Problem: [60. 排列序列](https://leetcode.cn/problems/permutation-sequence/description/)

# 思路

>

# Code1 官方方法，6

```Python []

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1]
        for i in range(1,n):
            factorial.append(factorial[-1]*i)

        k -= 1
        res = list()
        valid = [1] * (n + 1)
        for i in range(1, n + 1):
            order = k // factorial[n - i] + 1 #首个元素
            for j in range(1, n + 1):
                order -= valid[j]
                if order == 0:
                    res.append(str(j))
                    valid[j] = 0
                    break
            k %= factorial[n - i]
        return ''.join(res)
```

# Code2 根据之前的那道题自己想的。 但当 n=9 时会超时

```Python []
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        nums = [str(i+1) for i in range(n)]
        def dfs(temp,nums):
            if len(temp) == n:
                res.append(''.join(temp))
                if len(res)==k:
                    return res[k-1]
            else:
                for i in range(len(nums)):
                    dfs(temp+[nums[i]],nums[:i]+nums[i+1:])
        dfs([],nums)

        return res[k-1]
```
