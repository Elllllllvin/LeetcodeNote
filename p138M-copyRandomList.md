> Problem: [138. 复制带随机指针的链表](https://leetcode.cn/problems/copy-list-with-random-pointer/description/)

# 思路

> 和 clone 图的那道题换汤不换药

# 复杂度

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

# Code

```Python []

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        vis = {}

        res = pre = Node(-1)
        node = head

        while node:
            new_node = Node(node.val)
            vis[node] = new_node
            pre.next = new_node
            node = node.next
            pre = pre.next
        node = head
        p = res.next
        while node:
            if node.random:
                p.random = vis[node.random]
            else:
                p.random = None
            node = node.next
            p = p.next
        return res.next
```
