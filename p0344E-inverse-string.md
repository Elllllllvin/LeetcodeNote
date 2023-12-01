> Problem: [344. 反转字符串](https://leetcode.cn/problems/reverse-string/description/)

[toc]

# 思路

> 讲述看到这一题的思路

# 解题方法

> 描述你的解题方法

# 复杂度

- 时间复杂度: $O(n)$

- 空间复杂度: $O(1)$

# Code

```Python


class Solution:

    def reverseString(self, s: List[str]) -> None:

        """

        Do not return anything, modify s in-place instead.

        """

        n = len(s)

        for i in range(n//2):

            s[i],s[n-i-1] = s[n-i-1],s[i]

```
