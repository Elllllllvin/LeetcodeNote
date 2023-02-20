_Italic_> Problem: [199. 二叉树的右视图](https://leetcode.cn/problems/binary-tree-right-side-view/description/)

# 思路

层序遍历！
把每一层最后一个元素的值存到 res 中

# Code1

```Python
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            n = len(queue)
            for i in range(n):
                p = queue.pop(0)
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
                if i == n - 1:
                    res.append(p.val)
        return res
```
