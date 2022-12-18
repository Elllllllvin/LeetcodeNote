> Problem: [160. 相交链表](https://leetcode.cn/problems/intersection-of-two-linked-lists/description/)

# 思路

> 1.哈希表 2.标答

# Code1 hash 表

- 时间复杂度: $O(max(m,n))$
- 空间复杂度: $O(n)$

```Python []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        l1 = {}
        while p1:
            l1[p1] = 1
            p1=p1.next
        while p2:
            if p2 in l1.keys():
                return p2
            p2 = p2.next
        return None
```

# Code2 官方答案

- 时间复杂度: $O(m+n)$
- 空间复杂度: $O(1)$

```Python []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        while p1!=p2:
            if p1 == None:
                p1 = headB
            else:
                p1 = p1.next
            if p2 == None:
                p2 = headA
            else:
                p2 = p2.next

        return p1
```
