> Problem: [116. 填充每个节点的下一个右侧节点指针](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/description/)

[TOC]

# 思路

> 层序遍历 1.使用指针（优化空间） 2.使用 queue

# Code1 层序遍历（优化空间）（空间 O(1)）

- 时间复杂度: $O(n)$

- 空间复杂度: $O(1)$

```Python []

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        leftmost = root

        while leftmost.left:
            head = leftmost

            while head:
                head.left.next = head.right

                if head.next:
                    head.right.next = head.next.left

                head = head.next
            leftmost = leftmost.left

        return root

```

# Code2 层序遍历（空间 O(n)）

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n)$

```Python []

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        queue = [root]

        while queue:
            n = len(queue)
            pre = None
            for i in range(n):
                node = queue.pop(0)
                if i>0:
                    pre.next = node
                pre = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


        return root

```
