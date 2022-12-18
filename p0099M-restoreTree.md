> Problem: [99. 恢复二叉搜索树](https://leetcode.cn/problems/recover-binary-search-tree/description/)

# 思路

> 迭代，栈的思想

# 复杂度

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n)$

# Code

```Python []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 中序遍历的遍历元素是递增的
        firstnode = None
        secondnode = None
        pre = TreeNode(float("-inf"))

        p = root
        stack =[]
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()

            if firstnode == None and p.val < pre.val:
                firstnode = pre
            if firstnode and p.val < pre.val:
                secondnode = p
            pre = p
            p = p.right
        firstnode.val,secondnode.val = secondnode.val,firstnode.val
```
