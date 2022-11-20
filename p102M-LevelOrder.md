> Problem: [102. 二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/description/)

# 解题方法

> 1.dfs：使用递归实现
> 2.bfs：使用队列实现

# 复杂度

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n)$

# Code1 dfs

```Python []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        def dfs(height,root):
            if root == None:
                return
            if height +1 > len(res):
                res.append([])
            res[height].append(root.val)
            dfs(height + 1 , root.left)
            dfs(height + 1 , root.right)
        dfs(0,root)

        return res

```

# Code2 bfs

```Python []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = []
        queue.append(root)
        while queue:
            level = []
            for i in range(len(queue)):
                p = queue.pop(0)
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
                level.append(p.val)
            res.append(level)

        return res

```
