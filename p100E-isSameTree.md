> Problem: [100. 相同的树](https://leetcode.cn/problems/same-tree/description/)

[TOC]

# 思路

> dfs 深度优先搜索

# 复杂度

- 时间复杂度: $O(min(m,n))$

- 空间复杂度: $O(min(m,n))$ 空间复杂度取决于递归调用的层数，递归调用的层数不会超过较小的二叉树的最大高度，最坏情况下，二叉树的高度等于节点数。

# Code

```Python []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and not q) or (q and not p):
            return False
        elif p == q == None:
            return True

        if p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False
```
