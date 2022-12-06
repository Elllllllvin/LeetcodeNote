> Problem: [142. 环形链表 II](https://leetcode.cn/problems/linked-list-cycle-ii/description/)

# 思路

> 哈希表

# 复杂度

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n)$

# Code

```Python []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vis = {}
        p = head
        while p and p not in vis.keys():
            vis[p] = 1
            p = p.next

        return p

```
