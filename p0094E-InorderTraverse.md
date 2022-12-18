> Problem: [94. 二叉树的中序遍历（三种遍历迭代通用公式）](https://leetcode.cn/problems/binary-tree-inorder-traversal/description/)

# 思路

> 1.递归 2.迭代遍历

# 解题方法

“颜色标记法”，兼具栈迭代方法的高效，又像递归方法一样简洁易懂，更重要的是，这种方法对于前序、中序、后序遍历，能够写出完全一致的代码。

其核心思想如下：

- 使用颜色标记节点的状态，新节点为白色，已访问的节点为灰色。
- 如果遇到的节点为白色，则将其标记为灰色，然后将其右子节点、自身、左子节点依次入栈。
- 如果遇到的节点为灰色，则将节点的值输出。

# 复杂度

- 时间复杂度: $O(logn)$

- 空间复杂度: $O(n)$

# Code1 递归

```Python []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(node):
            if node == None:
                return
            if node.left != None:
                inorder(node.left)
            res.append(node.val)

            if node.right!= None:
                inorder(node.right)
        inorder(root)
        return res

```

# Code2 别人的神仙方法:迭代通用公式（前中后序遍历只需改变入栈顺序即可）

```Python []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        WHITE,GRAY = 0,1
        stack = [(WHITE,root)]
        while stack:
            color,node = stack.pop()
            if node == None:
                continue
            if color == WHITE:
                stack.append((WHITE,node.right))
                stack.append((GRAY,node))
                stack.append((WHITE,node.left))
            elif color == GRAY:
                res.append(node.val)

        return res


        return res
```
