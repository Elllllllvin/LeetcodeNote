> Problem: [89. 格雷编码](https://leetcode.cn/problems/gray-code/description/)

# Code1 递归

```Python []

class Solution:
    def grayCode(self, n: int) -> List[int]:
        def gray(n):
            if n==1:
                return ['0','1']
            LastList = gray(n-1)
            res = ['0'+item for item in LastList]+ ['1'+item for item in LastList][::-1]
            return res
        res = gray(n)
        for i in range(len(res)):
            res[i] = int(res[i],2)
        return res
```

# Code2 公式法

```Python []
class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0] * (1 << n)
        for i in range(1 << n):
            ans[i] = (i >> 1) ^ i
        return ans

```
