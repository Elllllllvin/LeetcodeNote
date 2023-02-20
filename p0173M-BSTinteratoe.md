_Italic_> Problem: [173.二叉树搜索迭代器](https://leetcode.cn/problems/binary-search-tree-iterator/description/)

# 思路

> 把该二叉树用中序遍历跑一遍，存到一个数组中

# 复杂度

- 时间复杂度: $O(n)$

- 空间复杂度:$O(n)$

# Code

```Python []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.res = []
        self.cnt = 0
        def dfs(root):
            if not root:
                return
            if root.left:
                dfs(root.left)
            self.res.append(root.val)
            if root.right:
                dfs(root.right)
        dfs(root)

    def next(self) -> int:
        self.cnt+=1
        return self.res[self.cnt-1]

    def hasNext(self) -> bool:
        if self.cnt<len(self.res):
            return True
        else:
            return False



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```
