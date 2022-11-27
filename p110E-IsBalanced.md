> Problem: [110. 平衡二叉树](https://leetcode.cn/problems/balanced-binary-tree/description/)

# Code1 递归

# 复杂度

- 时间复杂度: $O(n^2)$

```Python []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return abs(self.height(root.right)-self.height(root.left))<2 and self.isBalanced(root.left) and self.isBalanced(root.right)
	# 求高度
    def height(self, node):
        if not node:
            return 0
        return 1+max(self.height(node.right),self.height(node.left))
```

# Code2 优化一下

- 时间复杂度: $O(n)$

```Python []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.res = True #设置一个全局变量
        def helper(root):
            if not root:
                return 0
            left = helper(root.left) + 1
            right = helper(root.right) + 1
            #print(right, left)
            if abs(right - left) > 1:
                self.res = False
            return max(left, right)
        helper(root)
        return self.res

```
