> Problem: [338. 比特位计数](https://leetcode.cn/problems/counting-bits/description/)

[toc]

# 思路

> 动态规划 + 位运算

# 复杂度

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n)$

# Code

```Python3


class Solution:

    def countBits(self, n: int) -> List[int]:

        ans = [0]*(n+1)

        tmp = 0

        for i in range(1,n+1):

            if i==2**tmp:

                ans[i] = 1

                tmp += 1

            else:

                ans[i] = ans[2**(tmp-1)] + ans[i-2**(tmp-1)]


        return ans


```
