> Problem: [331. 验证二叉树的前序序列化](https://leetcode.cn/problems/verify-preorder-serialization-of-a-binary-tree/description/)

[toc]

# 思路

> 利用堆的思想
>
# 解题方法

> 描述你的解题方法

# 复杂度

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n)$

# Code

```Python


  class Solution:

    def isValidSerialization(self, preorder: str) -> bool:

        l = preorder.split(',')

        stack = []

        for i in range(len(l)):

            stack.append(l[i])

            while len(stack) >=3 and stack[-1]==stack[-2]=='#' and stack[-3]!='#':

                stack.pop()

                stack.pop()

                stack.pop()

                stack.append('#')


        return stack == ['#']



```
