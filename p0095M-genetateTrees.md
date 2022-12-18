> Problem: [95. 不同的二叉搜索树 II](https://leetcode.cn/problems/unique-binary-search-trees-ii/description/)

[TOC]

# 思路

> 不会，看的答案。。。

# Code

```Python []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(start,end):
            allTrees =[]
            if start > end :
                return [None,]

            for i in range(start,end+1):
                lefttree = dfs(start,i-1)
                righttree = dfs(i+1,end)

                for l in lefttree:
                    for r in righttree:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)
            return allTrees
        if n == 0:
            return []
        else:
            return dfs(1,n)



```
