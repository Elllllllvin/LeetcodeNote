> Problem: [86. 分隔链表](https://leetcode.cn/problems/partition-list/description/)

# 思路

> 链表排序题。没啥好说的

# 解题方法

我好蠢啊！！！原地修改还在沾沾自喜！！结果维护两个列表最后连起来就行了！！！！气死！！！！！

# Code

```Python []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if x<-100 or x>100 or head==None or head.next == None:
            return head

        q_more = p = head
        q_less = ListNode(-1)
        q_less.next = head
        pivot = q_less
        while p!=None and p.val < x:
            q_less = p
            p = p.next
        while p!=None:
            while p!=None and p.val >= x:
                q_more = p
                p = p.next
            if p!= None:
                q_more.next = p.next
                p.next = q_less.next
                q_less.next = p

                q_less = q_less.next
                p = q_more.next


        return pivot.next


```
