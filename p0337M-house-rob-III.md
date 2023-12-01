> Problem: [337. 打家劫舍 III](https://leetcode.cn/problems/house-robber-iii/description/)

[toc]

# 思路

> 树形DP

# 解题方法

> dfs深度优先搜索 + dp思想
# 复杂度

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n)$

# Code

```Python


# Definition for a binary tree node.

# class TreeNode:

#     def __init__(self, val=0, left=None, right=None):

#         self.val = val

#         self.left = left

#         self.right = right

class Solution:

    def rob(self, root: Optional[TreeNode]) -> int:


        def dfs(node):

            if node is None:

                return 0,0

            l_rob,l_not_rob = dfs(node.left)

            r_rob,r_not_rob = dfs(node.right)

            rob = node.val+l_not_rob+r_not_rob

            not_rob = max(l_rob,l_not_rob)+ max(r_rob,r_not_rob)

            return rob,not_rob


        return max(dfs(root))







```