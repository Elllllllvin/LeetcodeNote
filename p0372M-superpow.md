> Problem: [372. 超级次方](https://leetcode.cn/problems/super-pow/description/)

[toc]

# 思路

> 递归+幂运算

# 解题方法

> 描述你的解题方法

# 复杂度

- 时间复杂度: 对每个bi计算快速幂的时间为$O(log⁡bi)$

- 空间复杂度:

>  $O(1)$

# Code

```Python3


class Solution:

    def mypow(self,a,k):

        if k == 0:

            return 1

        if k%2 == 1:

            return (a* self.mypow(a,k-1)) % 1337

        else:

            sub = self.mypow(a,k//2)

            return (sub*sub)%1337



    def superPow(self, a: int, b: List[int]) -> int:

        if len(b) == 0:

            return 1

        e = b[-1]

        part1 = self.mypow(a,e)

        part2 = self.mypow(self.superPow(a,b[:-1]),10)

        return int(( part1 * part2 ) % 1337)


```
