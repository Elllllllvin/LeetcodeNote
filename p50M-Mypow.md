> Problem: [50. Pow(x, n)](https://leetcode.cn/problems/powx-n/description/)

# 思路

> 快速幂迭代+递归

# 复杂度

- 时间复杂度:

  > $O(logn)$

- 空间复杂度:
  > $O(logn)$

# Code

```Python []

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return self.myPow(1/x,-n)
        else:
            y = self.myPow(x,n//2)
            if(n%2 == 0):
                return y*y
            elif(n%2 == 1):
                return x*y*y

```
