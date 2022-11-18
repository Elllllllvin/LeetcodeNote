> Problem: [92. 反转链表 II](https://leetcode.cn/problems/reverse-linked-list-ii/description/)

# 思路

> 自己做的，只遍历一遍

# Code

```Python3 []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        p = res = head
        l= 1
        if left>l:
            anshead = ListNode(0)
            anshead.next = ListNode(0)
            ans = anshead.next
        else:
            ans = anshead = ListNode(0)
        while l<left:
            ans.val = p.val
            if l<left-1:
                ans.next = ListNode(0)
                ans = ans.next
            l += 1
            p = p.next

        flag = 1
        while l<=right:
            l += 1
            temp = ListNode(0)
            temp.val = p.val
            temp.next = ans.next
            ans.next = temp
            if flag == 1:
                res = ans.next
                flag = 0
            p = p.next
        print(p)
        while p!=None:
            res.next = ListNode(p.val)
            p = p.next
            res = res.next

        return anshead.next
```
