> Problem: [101. 对称二叉树](https://leetcode.cn/problems/symmetric-tree/description/)

# 思路

> 1.递归（深度优先搜索） 2.迭代

# Code1 递归（深度优先搜索）

```Python []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(p,q):
            if not p and not q:
                return True
            elif not q and p or not p and q:
                return False
            else:
                # print(p,q)
                return p.val == q.val and check(p.left,q.right) and check(p.right,q.left)
        if not root :
            return True
        else:
            return check(root.left,root.right)

```

# Code2 迭代

```Python []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right):
            return True

        queue = [root.left , root.right]
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)
            if not (left or right):
                continue
            if not (left and right):
                return False
            if left.val != right.val:
                return False

            queue.append(left.left)
            queue.append(right.right)

            queue.append(left.right)
            queue.append(right.left)

        return True
```
