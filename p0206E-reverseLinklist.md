_Italic_> Problem: [206. 反转列表](https://leetcode.cn/problems/reverse-linked-list/description/)

# 思路

1.迭代

2.递归

# Code1 迭代

时间复杂度：o(n)

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = head
        if not head:
            return head
        p = head.next
        head.next = None
        while p:
            q = p
            p = p.next
            q.next = front
            front = q
        return front
```

# Code2 递归

```Python
def reverseList(self, head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head

    p = self.reverseList(head.next)
    head.next.next = head
    head.next = None

    return p

```
