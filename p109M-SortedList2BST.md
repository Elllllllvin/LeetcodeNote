> Problem: [109. 有序链表转换二叉搜索树](https://leetcode.cn/problems/convert-sorted-list-to-binary-search-tree/description/)

# 解题方法

- 1.108 题的延申：先将链表里的值放到数组中，然后分治

- 2.快慢指针:快慢指针起初都指向头结点，分别一次走两步和一步，当快指针走到尾结点时，慢指针正好走到链表中间。然后断为两个链表，分而治之。

# Code1 108 题的延申

- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

```Python []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def buildTree(nums):
            if not nums:
                return None
            mid = len(nums)//2
            root = TreeNode(nums[mid])
            root.left = buildTree(nums[:mid])
            root.right = buildTree(nums[mid+1:])
            return root
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return buildTree(nums)
```

# Code2 快慢指针

- 时间复杂度: $O(nlogn)$
- 空间复杂度: $O(logn)$ 递归栈的深度

```Python []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def findmid(head, tail):
            slow = head
            fast = head
            while fast != tail and fast.next!= tail :
                slow = slow.next
                fast = fast.next.next
            return slow

        def helper(head, tail):
            if  head == tail: return
            node = findmid(head, tail)
            root = TreeNode(node.val)
            root.left = helper(head, node)
            root.right = helper(node.next, tail)
            return root

        return helper(head, None)

```
