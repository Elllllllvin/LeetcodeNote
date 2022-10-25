> Problem: [23. 合并 K 个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists/description/)

# Code1 优先级队列

自己想的。。过了就行，时间空间都不太好 30%左右的样子

```Python []
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if(len(lists)==0 or lists == None):
            return None
        headnodeVal = [0]*len(lists)
        for i in range(len(lists)):
            if lists[i] == None:
                headnodeVal[i] = 10001
            else:
                headnodeVal[i] = lists[i].val #初始化
        # print(headnodeVal)
        head = ListNode(0)
        res = head
        while True:
            # print(headnodeVal)
            minval = min(headnodeVal)
            if(minval==10001):
                break
            i = headnodeVal.index(minval)
            head.next = ListNode(0)
            head.next.val = lists[i].val
            head = head.next
            lists[i] = lists[i].next
            if(lists[i]==None):
                lists[i] = ListNode(10001)
            headnodeVal[i] = lists[i].val
        return res.next
```

# Code2 分而治之的思想

```Python []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:return
        n = len(lists)
        return self.merge(lists, 0, n-1)
    def merge(self,lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.mergeTwoLists(l1, l2)
    def mergeTwoLists(self,l1, l2):
        if not l1:return l2
        if not l2:return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
```
