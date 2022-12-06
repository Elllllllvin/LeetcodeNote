> Problem: [129. 求根节点到叶节点数字之和](https://leetcode.cn/problems/sum-root-to-leaf-numbers/description/)

# 思路

> 挺简单的一道 dfs

# Code

```Python []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(tempSum,root):
            if not root:
                return
            if not root.left and not root.right:
                self.res += tempSum*10 + root.val
                return

            if root.left:
                dfs(tempSum*10+root.val,root.left)
            if root.right:
                dfs(tempSum*10+root.val,root.right)
            return
        dfs(0,root)
        return self.res

```
