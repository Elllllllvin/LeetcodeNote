class ListNode:
    def __init__(self,val = 0,next=None) -> None:
        self.val = val
        self.next = None
class Linklist:
    def __init__(self) -> None:
        self.head = None
    def initlist(self,data):
        self.head = ListNode(data[0])
        r = self.head
        p = self.head
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r
    def convertlist(self,head):
        ret = []
        if head == None:
            return
        node  = head
        while node != None:
            ret.append(node.val)
            node = node.next
        return ret

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = ListNode()
        head = l
        cf = 0
        while(True):
            s = 0
            s =  l1.val + l2.val + cf
            if s>9:
                s = s-10
                cf = 1
            else :
                cf = 0
            l.val = s
            if l1.next is None and l2.next is None:
                if cf==1:
                    l.next = ListNode(1)
                break
            l.next = ListNode()
            if l1.next is None:
                l1.next = ListNode()
            elif l2.next is None:
                l2.next = ListNode()
            l1 = l1.next
            l2 = l2.next
            l = l.next
        return head

l = Linklist()
list1 = [2,4,3]
list2 = [5,6,4]
l1 = l.initlist(list1)
l2 = l.initlist(list2)
s = Solution()
print(l.convertlist(s.addTwoNumbers(l1, l2)))