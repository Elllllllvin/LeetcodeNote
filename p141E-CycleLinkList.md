> Problem: [141. 环形链表](https://leetcode.cn/problems/linked-list-cycle/description/)

[TOC]

# 思路

> 用字典存储比 list 的 append 快了很多，可能是因为字典的 key 使是只存地址，list 还要村内容

# Code1 没啥好说的

- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

```Python []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        vis = {}
        p = head
        while p and p not in vis.keys():
            vis[p] = 1
            p = p.next
        return p != None


```

# Code2 优化空间

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

```Python []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p = head
        while p and p.val!=100001:
            p.val = 100001
            p = p.next
        return p != None

```
