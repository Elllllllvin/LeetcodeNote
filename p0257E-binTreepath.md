> Problem: [257. 二叉树的所有路径](https://leetcode.cn/problems/binary-tree-paths/description/)

[TOC]

# 思路
> 
> dfs

# Code
```Python []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(root,path):
            if path =='':
                path = str(root.val)
            else:
                path += '->'+str(root.val)

            if root.left == None and root.right == None:
                res.append(path)
                return
            
            if root.left:
                dfs(root.left,path)
            
            if root.right:
                dfs(root.right,path)
            return 
        dfs(root,'')

        return res


```
