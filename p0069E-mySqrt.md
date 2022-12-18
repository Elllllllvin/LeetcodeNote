> Problem: [69. x 的平方根 ](https://leetcode.cn/problems/sqrtx/description/)

# 解题方法

> 法一：二分查找法
> 法二：牛顿迭代法

# Code1 二分查找

```Python []

class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==1:
            return 1
        left,right = 0,x
        ans = -1
        while(left<=right):
            mid = (left+right)//2
            if mid*mid<=x:
                ans = mid
                left = mid + 1

            else:
                right = mid -1
        return ans

```

# Code2 牛顿迭代法

```Python []
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        C, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi
        return int(x0)
```
