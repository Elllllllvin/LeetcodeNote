> Problem: [字节面试 148. 排序链表](https://leetcode.cn/problems/sort-list/description/)

# 思路

1.归并排序：自顶向下

2.（字节面试）规定空间复杂度为 O(1)的算法：自底向上

# 复杂度

# Code 1 自顶向下的归并排序

- 时间复杂度: $O(nlogn)$
- 空间复杂度: $O(logn)$ 递归使用的栈空间

```Python []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def sortFunc(head,tail):
            if not head:
                return head #空链表
            if head.next == tail:
                head.next = None #链表个数为1个
                return head
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return merge(sortFunc(head,mid),sortFunc(mid,tail))

        def merge(head1,head2):
            dummyhead = ListNode(0)
            temp,temp1,temp2 = dummyhead,head1,head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            if temp2:
                temp.next = temp2

            return dummyhead.next
        return sortFunc(head,None)
```

# Code2 自底向下

- 时间复杂度: $O(nlogn)$
- 空间复杂度: $O(1)$ 递归使用的栈空间

```Python []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(head1,head2):
            dummyhead = ListNode(0)
            temp,temp1,temp2 = dummyhead,head1,head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            if temp2:
                temp.next = temp2

            return dummyhead.next

        if not head:
            return head

        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        # 遍历链表，O(n)

        dummyHead = ListNode(0)
        dummyHead.next = head
        subLength = 1
        while subLength<length:
            prev,curr = dummyHead,dummyHead.next
            while curr:
                head1 = curr
                for i in range(1,subLength):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                head2 = curr.next
                curr.next = None
                curr = head2
                for i in range(1,subLength):
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break
                succ = None
                if curr:
                    succ = curr.next
                    curr.next = None
                merged = merge(head1,head2)
                prev.next = merged
                while prev.next:
                    prev = prev.next
                curr = succ
            subLength *= 2
        return dummyHead.next
```
