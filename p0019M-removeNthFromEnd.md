> Problem: [19. 删除链表的倒数第 N 个结点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/)

# 思路

> 分类讨论

# 解题方法

> 分为：
> 1：只有一个节点的情况，n 只能为 1
> 2：常见情况（删除链表中间的节点）
> 3：删除头节点情况
> 4：删除尾节点情况

# 复杂度

- 时间复杂度:

  > 添加时间复杂度, 示例： $O(n)$

- 空间复杂度:
  > 添加空间复杂度, 示例： $O(1)$

# Code

79.51% 52.5%

```Python []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n) :
        # pivot = ListNode()
        # pivot.next = head
        p = head
        t = head
        cnt = 0
        if(n == 1):
            if(p.next == None):#只有一个节点的情况，n只能等于1
                head = None
            else:
                while(p.next.next!= None):#多个节点情况，n=1删除尾节点
                    p = p.next
                p.next = None

        else:
            while(p.next != None):
                if(cnt == n):
                    t = t.next
                    cnt -= 1
                cnt += 1
                p = p.next
            if (cnt == n): # common情况
                t.next = t.next.next
            else: #删除头节点情况
                head = head.next
        return head
```
