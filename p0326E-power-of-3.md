> Problem: [326.3的幂](https://leetcode.cn/problems/power-of-three/)

# 解题方法

1.递归
2.计算对数（不用递归或者迭代）

# 复杂度

- 时间复杂度: O(nlogn)
- 空间复杂度：O(n)


# Code1

```Python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n and n % 3 == 0:
            n //= 3
        return n == 1

作者：力扣官方题解
链接：https://leetcode.cn/problems/power-of-three/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

# Code2

```Python
import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        x = math.log(n,3)
        return True if abs(x-round(x))<10**-10 else False
```
